# Property inspector helpers. Rows are 31 px high; scrollbox y of row n (0-based) = 16 + 31*n.
$global:INSP = [IntPtr]1641924
function Insp-Editor {
  foreach($k in [IQ]::Kids($global:INSP)){
    if(-not [IQ]::IsWindowVisible($k)){ continue }
    $r=New-Object IQ+RECT; [IQ]::GetWindowRect($k,[ref]$r)|Out-Null
    $ir=New-Object IQ+RECT; [IQ]::GetWindowRect($global:INSP,[ref]$ir)|Out-Null
    if($r.L -lt $ir.L + 150){ continue }   # value column only (relative to the inspector, works on any monitor)
    $c=[IQ]::Cls($k)
    if($c -eq 'Edit' -or $c -eq 'TEdit'){ return $k }
  }
  return $null
}
function Insp-Set([int]$row,[string]$val){
  $y = [int]((16 + 31*$row)*$global:SC)
  IQ-DblClick $global:INSP 305 $y; Start-Sleep -Milliseconds 700
  $ed = Insp-Editor
  if(-not $ed){ throw "no editor at row $row" }
  [IQ]::SendMessage($ed,0x000C,[IntPtr]0,$val)|Out-Null; Start-Sleep -Milliseconds 200
  IQ-Key $ed 0x0D; Start-Sleep -Milliseconds 700
}
function Insp-Shot($name='insp'){ IQ-Shot 10685056 "C:\Users\Sav78\Documents\testia_sandbox\gui\$name.png" | Out-Null }
# Variants taking the y coordinate measured on an inspector screenshot (insp.png): scrollbox y = shot_y - 58
function Insp-SetY([int]$shotY,[string]$val){
  IQ-DblClick $global:INSP 305 ($shotY-$global:INSPOFF); Start-Sleep -Milliseconds 700
  $ed = Insp-Editor; if(-not $ed){ throw "no editor at y $shotY" }
  [IQ]::SendMessage($ed,0x00B1,[IntPtr]0,[IntPtr](-1))|Out-Null
  IQ-Chars $ed $val; Start-Sleep -Milliseconds 300
  IQ-Key $ed 0x0D; Start-Sleep -Milliseconds 700
}

function Insp-Esc { $e=Insp-Editor; if($e){ IQ-Key $e 0x1B; Start-Sleep -Milliseconds 300 } }
