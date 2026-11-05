# Rejoue un scenario dans IQANsimulate avec les modeles d'equipements, enregistre les canaux
# observes et les paires ancienne logique / v2, puis lance la comparaison.
#   powershell -File rejouer.ps1 -Scenario scenarios\E_demarrage.json -Projet <copie.idax>
#   powershell -File rejouer.ps1 -Scenario scenarios\E_demarrage.json -Fake   (essai sans simulateur)
# Regles : copie du projet seulement, jamais le .idax d'origine ; aucun controleur n'est connecte.
param(
    [Parameter(Mandatory)][string]$Scenario,
    [string]$Projet = "$env:USERPROFILE\Documents\testia_sandbox\jumeau\v2_lot8.idax",
    [string]$Sortie = "$env:USERPROFILE\Documents\testia_sandbox\jumeau\resultats",
    [double]$Periode = 0.1,
    [switch]$Fake
)
$ErrorActionPreference = 'Stop'
[Threading.Thread]::CurrentThread.CurrentCulture = [Globalization.CultureInfo]::InvariantCulture
. "$PSScriptRoot\simcom.ps1"
. "$PSScriptRoot\modeles.ps1"

if ($Projet -match '\\testia\\[^\\]+\.idax$' -and $Projet -notmatch 'sandbox') { throw "Refus : $Projet ressemble a un projet d'origine. Utiliser une copie dans testia_sandbox." }

$sc = Get-Content (Resolve-Path $Scenario) -Raw -Encoding UTF8 | ConvertFrom-Json
$profil = Get-Content (Join-Path $PSScriptRoot "profils\$($sc.profil).json") -Raw -Encoding UTF8 | ConvertFrom-Json
$variante = $sc.profil.Substring(0, 1)
$paires = Import-Csv (Join-Path $PSScriptRoot 'paires_ancien_v2.csv') -Delimiter ';' | Where-Object { $_.variante -in '*', $variante }

$s = [SimCom]::new([bool]$Fake)
$s.Ouvrir((Resolve-Path $Projet).Path)
$bus = @{ tension_bus = 0; tension_pack = 0; courant_traction = 0; courant_pompe = 0; courant_charge = 0; soc = 0 }
$modeles = New-Modeles $s $profil $bus
$etat = @{}; if ($sc.etat_initial) { $sc.etat_initial.PSObject.Properties | ForEach-Object { $etat[$_.Name] = $_.Value } }
foreach ($m in $modeles.Values) { $m.Init($etat) }

# Reglages du bateau : parametres du profil puis ceux du scenario.
$reglages = [ordered]@{}
foreach ($src in $profil.parametres, $sc.parametres) { if ($src) { $src.PSObject.Properties | ForEach-Object { $reglages[$_.Name] = $_.Value } } }
foreach ($k in $reglages.Keys) { try { $s.Ecrire($k, [double]$reglages[$k]) } catch { Write-Warning "Reglage $k non ecrit : $($_.Exception.Message)" } }

# Colonnes enregistrees : observes du scenario + paires presentes dans le simulateur.
$colonnes = New-Object System.Collections.ArrayList
foreach ($c in @($sc.observer) + @($paires | ForEach-Object { $_.v2; $_.ancien })) {
    if ($c -and -not $colonnes.Contains($c)) { if ($s.Existe($c)) { [void]$colonnes.Add($c) } else { Write-Warning "Non enregistre (absent ou ambigu) : $c" } }
}

New-Item -ItemType Directory -Force $Sortie | Out-Null
$base = Join-Path $Sortie ("{0}_{1:yyyyMMdd_HHmmss}" -f [IO.Path]::GetFileNameWithoutExtension($Scenario), (Get-Date))
$journal = [IO.StreamWriter]::new("$base.csv", $false, [Text.Encoding]::UTF8)
$journal.WriteLine((@('t_s') + $colonnes + @('bus_soc', 'bus_tension', 'bus_courant')) -join ';')

$evenements = @($sc.evenements | Sort-Object { [double]$_.t })
$prochain = 0
$pas = [Math]::Max(1, [int][Math]::Round($Periode * 1000 / $s.Cycle))
$dt = $pas * $s.Cycle / 1000.0
$s.Demarrer()
try {
    for ($t = 0.0; $t -le [double]$sc.duree_s + 1e-9; $t += $dt) {
        while ($prochain -lt $evenements.Count -and [double]$evenements[$prochain].t -le $t + 1e-9) {
            $e = $evenements[$prochain]; $prochain++
            switch ($e.action) {
                'ecrire'   { $s.Ecrire($e.canal, [double]$e.valeur) }
                'touche'   { $modeles.clavier.Appuyer($e.touche, $(if ($e.duree) { [double]$e.duree } else { 0.5 })) }
                'secteur'  { $modeles.chargeur.Secteur = [bool]$e.valeur }
                'panne'    { $modeles[$e.equipement].Panne($e.type, $true) }
                'retablir' { $modeles[$e.equipement].Panne($e.type, $false) }
                default    { Write-Warning "Action inconnue : $($e.action)" }
            }
            Write-Host ("{0,6:N1} s  {1}" -f $t, ($e | ConvertTo-Json -Compress))
        }
        $bus.courant_traction = [double]$bus['courant_variateur_droit'] + [double]$bus['courant_variateur_gauche']
        foreach ($m in $modeles.Values) { $m.Pas($dt) }
        $s.Avancer($pas)
        $ligne = @('{0:F2}' -f $t) + @($colonnes | ForEach-Object { try { '{0:G6}' -f $s.Lire($_) } catch { 'ERR' } })
        $ligne += @(('{0:F2}' -f [double]$bus.soc), ('{0:F1}' -f [double]$bus.tension_bus), ('{0:F1}' -f [double]$bus.courant_batterie))
        $journal.WriteLine($ligne -join ';')
    }
}
finally {
    $journal.Close()
    $s.Arreter()
}
"Journal : $base.csv"
$py = Join-Path $PSScriptRoot 'comparer.py'
python -I $py "$base.csv" (Join-Path $PSScriptRoot 'paires_ancien_v2.csv') (Resolve-Path $Scenario).Path "$base.md" $variante
