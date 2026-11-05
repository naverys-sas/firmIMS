# Lance "Project check" d'IQANdesign sur le projet ouvert (pilotage par messages, sans souris) et
# ecrit la liste des erreurs, avertissements et indices dans un fichier texte.
#   powershell -File verifier_projet.ps1 -ProcessId <pid IQANdesign> -Sortie check.txt
param([Parameter(Mandatory)][int]$ProcessId, [string]$Sortie = "$env:TEMP\project_check.txt")
. "$env:USERPROFILE\Documents\testia_sandbox\gui\iq.ps1"
. "$env:USERPROFILE\Documents\testia_sandbox\gui\lv.ps1"
$main = [IQ]::Tops([uint32]$ProcessId) | Where-Object { [IQ]::Cls($_) -eq 'TIQANdesignMainWindow' } | Select-Object -First 1
$tb = [IQ]::Kids($main) | Where-Object { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TToolBar' } | Select-Object -First 1
IQ-Click $tb 389 16   # bouton "Check" de la barre d'outils (coche), position relevee le 05/11/2026
$dlg = $null
for ($i = 0; $i -lt 60 -and -not $dlg; $i++) { Start-Sleep 1; $dlg = [IQ]::Tops([uint32]$ProcessId) | Where-Object { [IQ]::Cls($_) -eq 'TCheckApplDlg' } | Select-Object -First 1 }
if (-not $dlg) { throw "Pas de fenetre Project Check" }
Start-Sleep 2
$lv = [IQ]::Kids($dlg) | Where-Object { [IQ]::Cls($_) -eq 'TIQListView' } | Select-Object -First 1
$lignes = @(LV-Dump $lv 5)
$lignes | Set-Content $Sortie -Encoding UTF8
$fermer = [IQ]::Kids($dlg) | Where-Object { [IQ]::Cls($_) -eq 'TButton' -and [IQ]::Txt($_) -eq 'Close' }
if ($fermer) { [IQ]::PostMessage($fermer, 0xF5, [IntPtr]0, [IntPtr]0) | Out-Null }
"{0} erreurs, {1} avertissements, {2} lignes -> {3}" -f @($lignes | Where-Object { $_ -match '^Error' }).Count, @($lignes | Where-Object { $_ -match '^Warning' }).Count, $lignes.Count, $Sortie
