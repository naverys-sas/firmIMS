param([string]$outDir, [string[]]$modules)
. C:\Users\Sav78\Documents\testia_sandbox\gui\ops.ps1
. C:\Users\Sav78\Documents\testia_sandbox\gui\lv.ps1
New-Item -ItemType Directory -Force $outDir | Out-Null
foreach($m in $modules){
  $it = TV-Find $global:TVH @('System Layout', $m); [TV]::Visible($global:TVH,$it); [TV]::Select($global:TVH,$it); Start-Sleep 2
  $pc = @([IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TPageControl' })[0]
  IQ-Click $pc 140 10; Start-Sleep 2
  $lv = @([IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TListView' })[0]
  $safe = ($m -replace '[^\w\-]','_')
  "pin`tname`tchannel`tdescription" | Out-File -Encoding utf8 "$outDir\$safe.tsv"
  LV-Dump $lv 4 | Out-File -Encoding utf8 -Append "$outDir\$safe.tsv"
  "$m -> $([LV]::Count($lv)) rows"
}
