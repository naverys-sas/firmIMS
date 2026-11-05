# Ouvre la copie du projet dans IQANsimulate et liste tous ses canaux (nom, module, pilotable, unite).
# Sert a verifier les noms des profils avant de rejouer un scenario.
param(
    [string]$Projet = "$env:USERPROFILE\Documents\testia_sandbox\jumeau\v2_lot8.idax",
    [string]$Sortie = "$env:USERPROFILE\Documents\testia_sandbox\jumeau\inventaire.csv"
)
$ErrorActionPreference = 'Stop'
. "$PSScriptRoot\simcom.ps1"
$s = [SimCom]::new($false)
$s.Ouvrir((Resolve-Path $Projet).Path)
try {
    $s.Inventaire() | Select-Object Id, Nom, Module, Pilotable, Unite, SousType | Export-Csv $Sortie -Delimiter ';' -NoTypeInformation -Encoding UTF8
    "$($s.Info.Count) canaux, cycle $($s.Cycle) ms -> $Sortie"
    "Pilotables : " + @($s.Info.Values | Where-Object Pilotable).Count
    # Verification des noms utilises par les profils.
    foreach ($f in Get-ChildItem "$PSScriptRoot\profils\*.json") {
        $p = Get-Content $f.FullName -Raw -Encoding UTF8 | ConvertFrom-Json
        foreach ($sec in $p.PSObject.Properties | Where-Object { $_.Value.canaux }) {
            $noms = @($sec.Value.canaux.PSObject.Properties.Value) + @($sec.Value.trames)
            foreach ($n in $noms | Where-Object { $_ }) {
                $etat = if (-not $s.Existe($n)) { 'ABSENT OU AMBIGU' } elseif (-not $s.Info[$s.Id($n)].Pilotable) { 'lecture seule' } else { 'ok' }
                if ($etat -ne 'ok') { "$($f.BaseName) / $($sec.Name) : $n -> $etat" }
            }
        }
    }
}
finally { $s.Arreter() }
