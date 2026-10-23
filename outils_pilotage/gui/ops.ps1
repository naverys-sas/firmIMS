# Higher-level operations built on iq/insp/menu/pick helpers.
. C:\Users\Sav78\Documents\testia_sandbox\gui\iq.ps1
. C:\Users\Sav78\Documents\testia_sandbox\gui\insp.ps1
. C:\Users\Sav78\Documents\testia_sandbox\gui\menu.ps1
. C:\Users\Sav78\Documents\testia_sandbox\gui\pick.ps1
. C:\Users\Sav78\Documents\testia_sandbox\gui\tv.ps1
$global:IQPID = [int](Get-Content C:\Users\Sav78\Documents\testia_sandbox\gui\pid.txt)
$global:MAIN = [IntPtr](@([IQ]::Tops([uint32]$global:IQPID) | ? { [IQ]::Cls($_) -eq 'TIQANdesignMainWindow' })[0])

function Add-Channel([string]$search){
  $add=[IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TAdvSmoothButton' -and [IQ]::Txt($_) -eq 'Add' } | select -first 1
  IQ-Click $add 40 18; Start-Sleep 2
  $dlg=[IQ]::Tops([uint32]$global:IQPID) | ? { [IQ]::Cls($_) -eq 'TAddComponentDialog' } | select -first 1
  $ed=[IQ]::Kids($dlg) | ? { [IQ]::Cls($_) -eq 'TEdit' } | select -first 1
  [IQ]::SendMessage($ed,0x000C,[IntPtr]0,$search)|Out-Null; Start-Sleep 1
  IQ-Key $ed 0x0D; Start-Sleep 2
}
function Fn-Tabs { [IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TTabControl' } | select -first 1 }
function Fn-Editor { [IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TRichEditNew' } | select -first 1 }
# tabX: x of the tab label inside the tab control
function Fn-Qcode([int]$tabX,[string]$code){
  $t=Fn-Tabs; IQ-Click $t $tabX 16; Start-Sleep 1
  $re=Fn-Editor; IQ-Click $re 50 20; Start-Sleep -Milliseconds 300
  [IQ]::SendMessage($re,0x00B1,[IntPtr]0,[IntPtr](-1))|Out-Null
  IQ-Key $re 0x2E; Start-Sleep -Milliseconds 200   # delete selection
  $lines = $code -split "`r"
  for($i=0;$i -lt $lines.Count;$i++){
    if($i -gt 0){ IQ-Key $re 0x0D; Start-Sleep -Milliseconds 80; IQ-Key $re 0x24; Start-Sleep -Milliseconds 50 }  # Enter then Home (drop auto-indent effect)
    IQ-Chars $re $lines[$i]
  }
  Start-Sleep 1
}
function Shot-Fn($name='fi'){ $fi=[IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TFunctionInspector' } | select -first 1; IQ-Shot $fi "C:\Users\Sav78\Documents\testia_sandbox\gui\$name.png" | Out-Null }
function Shot-Main($name='main'){ IQ-Shot $global:MAIN "C:\Users\Sav78\Documents\testia_sandbox\gui\$name.png" | Out-Null }
function Save-Project { $tb=[IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TToolBar' } | Sort-Object { $r=New-Object IQ+RECT; [IQ]::GetWindowRect($_,[ref]$r)|Out-Null; $r.T } | select -first 1; $r=New-Object IQ+RECT; [IQ]::GetWindowRect($tb,[ref]$r)|Out-Null; $h=$r.B-$r.T; IQ-Click $tb ([int](66*$h/33)) ([int]($h/2)); Start-Sleep 4 }
function Close-Menus { 1..5 | % { $m=@(Menu-Windows $global:IQPID) | select -last 1; if($m){ IQ-Key $m 0x1B; Start-Sleep -Milliseconds 300 } } }

$global:COORDS = Get-Content -Raw -Encoding UTF8 C:\Users\Sav78\Documents\testia_sandbox\gui\coords.json | ConvertFrom-Json
$global:TVH = [IntPtr](@([IQ]::Kids($global:MAIN) | ? { [IQ]::Cls($_) -eq 'TIQANTreeView' })[0])
function Go-Group([string]$groupPath){
  $parts = @('Application Logic') + ($groupPath -split ' / ')
  $it = TV-Find $global:TVH $parts
  [TV]::Visible($global:TVH,$it); [TV]::Select($global:TVH,$it); Start-Sleep 2
}
function Insp-Name {
  IQ-DblClick $global:INSP 305 16; Start-Sleep -Milliseconds 600
  $e = Insp-Editor; $t = if($e){ [IQ]::Txt($e) } else { '' }
  if($e){ IQ-Key $e 0x1B; Start-Sleep -Milliseconds 300 }
  return $t
}
function Ch-Select([string]$groupPath,[string]$name){
  Go-Group $groupPath
  $list = $global:COORDS.$groupPath
  $target = $list | ? { $_[0] -eq $name } | select -first 1
  if(-not $target){ throw "channel $name not in coords for $groupPath" }
  $ctrls = [IQ]::Kids($global:MAIN) | ? { [IQ]::Cls($_) -eq 'TFGChannelControl' -and [IQ]::IsWindowVisible($_) }
  $rects = @{}; foreach($c in $ctrls){ $r=New-Object IQ+RECT; [IQ]::GetWindowRect($c,[ref]$r)|Out-Null; $rects["$c"]=$r }
  $votes=@{}
  foreach($c in $ctrls){ $r=$rects["$c"]; foreach($e in $list){ $k="$($r.L-[int][Math]::Round($e[2]*$global:SC)),$($r.T-[int][Math]::Round($e[3]*$global:SC))"; $votes[$k]=1+[int]$votes[$k] } }
  $best = ($votes.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 1).Key
  $ox,$oy = $best -split ','
  foreach($c in $ctrls){ $r=$rects["$c"]; if([Math]::Abs(($r.L - [int]$ox) - [Math]::Round($target[2]*$global:SC)) -le 1 -and [Math]::Abs(($r.T - [int]$oy) - [Math]::Round($target[3]*$global:SC)) -le 1){
      IQ-Click $c 60 10; Start-Sleep -Milliseconds 800
      $n = Insp-Name
      if($n -eq ''){ Start-Sleep -Milliseconds 500; $n = Insp-Name }
      if($n -eq $name){ return $c } } }
  # Fallback: try every control in the right column (x offsets are reliable), check its name
  foreach($c in $ctrls){ $r=$rects["$c"]; if([Math]::Abs(($r.L - [int]$ox) - [Math]::Round($target[2]*$global:SC)) -le 2){
      IQ-Click $c 60 8; Start-Sleep -Milliseconds 600
      if((Insp-Name) -eq $name){ return $c } } }
  throw "no control at $($target[2]),$($target[3]) for $name"
}

# Resolve handles that change with each IQANdesign process
$global:PI = @([IQ]::Kids($global:MAIN) | ? { [IQ]::Cls($_) -eq 'TPropertyInspectorDsgn' })[0]
$global:INSP = @([IQ]::Kids($global:PI) | ? { [IQ]::Cls($_) -eq 'TScrollBox' })[0]
function Insp-Shot($name='insp'){ IQ-Shot $global:PI "C:\Users\Sav78\Documents\testia_sandbox\gui\$name.png" | Out-Null }
function Fn-Lists { $fi=@([IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TFunctionInspector' })[0]
  $l=@([IQ]::Kids($fi) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TListBox' } | Sort-Object { $r=New-Object IQ+RECT; [IQ]::GetWindowRect($_,[ref]$r)|Out-Null; $r.L }); return $l }
function Fn-ObjBar { $fi=@([IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TFunctionInspector' })[0]; @([IQ]::Kids($fi) | ? { [IQ]::Cls($_) -eq 'TToolBar' })[0] }
# kind: single=150, math=320 (x on the object toolbar)
function Fn-AddObject([int]$listIndex,[string]$kind='single'){ $l=Fn-Lists; $n=[int][IQ]::SendMessage($l[$listIndex],0x018B,[IntPtr]0,[IntPtr]0); IQ-Click $l[$listIndex] 100 10; Start-Sleep -Milliseconds 300; [IQ]::SendMessage($l[$listIndex],0x0186,[IntPtr](-1),[IntPtr]0)|Out-Null; Start-Sleep -Milliseconds 500; $x= if($kind -eq 'math'){[int](320*$global:SC)}else{[int](145*$global:SC)}; IQ-Click (Fn-ObjBar) $x ([int](17*$global:SC)); Start-Sleep 1.5 }

function Set-FrameTimeout([string]$group,[string]$name,[string]$ms,[int]$y=198){
  Insp-Esc
  Ch-Select $group $name | Out-Null
  Insp-Esc; Insp-SetY $y $ms; IQ-Click $global:INSP 100 ([int](47*$global:SC)); Start-Sleep 1; Insp-Esc
  Insp-Shot ("to_" + ($name -replace '[^\w]','_'))
}

# Display scale (row heights) and inspector offset, recomputed each time ops.ps1 is loaded
$global:TBMAIN = @([IQ]::Kids($global:MAIN) | ? { [IQ]::IsWindowVisible($_) -and [IQ]::Cls($_) -eq 'TToolBar' } | Sort-Object { $r=New-Object IQ+RECT; [IQ]::GetWindowRect($_,[ref]$r)|Out-Null; $r.T })[0]
$tr=New-Object IQ+RECT; [IQ]::GetWindowRect($global:TBMAIN,[ref]$tr)|Out-Null
$global:SC = [Math]::Round(($tr.B-$tr.T)/33.0*20)/20.0   # 1.0, 0.8 ... (IQANdesign scales by steps)
$pr=New-Object IQ+RECT; [IQ]::GetWindowRect($global:PI,[ref]$pr)|Out-Null; $sr=New-Object IQ+RECT; [IQ]::GetWindowRect($global:INSP,[ref]$sr)|Out-Null
$global:INSPOFF = $sr.T - $pr.T
function Save-Project { IQ-Click $global:TBMAIN ([int](67*$global:SC*33/26*26/33)) ([int](($tr.B-$tr.T)/2)); Start-Sleep 4 }
"scale=$($global:SC) inspoff=$($global:INSPOFF)"
