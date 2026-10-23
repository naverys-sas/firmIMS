# Insp-Pick row path: open the channel menu of an inspector row and pick a channel by menu path.
function Insp-Pick([int]$row,[string[]]$path){
  $y = [int]((16 + 31*$row)*$global:SC)
  IQ-DblClick $global:INSP 305 $y; Start-Sleep -Milliseconds 800
  $cb=[IQ]::Kids($global:INSP) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TCompComboBox' } | select -first 1
  if(-not $cb){ throw "no combo at row $row" }
  $r=New-Object IQ+RECT; [IQ]::GetWindowRect($cb,[ref]$r)|Out-Null
  IQ-Click $cb ($r.R-$r.L-10) 10; Start-Sleep -Milliseconds 900
  Menu-Pick $global:IQPID $path
}
function Insp-PickY([int]$shotY,[string[]]$path){
  IQ-DblClick $global:INSP 305 ($shotY-$global:INSPOFF); Start-Sleep -Milliseconds 800
  $cb=[IQ]::Kids($global:INSP) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TCompComboBox' } | select -first 1
  if(-not $cb){ throw "no combo at y $shotY" }
  $r=New-Object IQ+RECT; [IQ]::GetWindowRect($cb,[ref]$r)|Out-Null
  IQ-Click $cb ($r.R-$r.L-10) 10; Start-Sleep -Milliseconds 900
  Menu-Pick $global:IQPID $path
}
function Insp-Esc { $e=Insp-Editor; if($e){ IQ-Key $e 0x1B; Start-Sleep -Milliseconds 300 } }
