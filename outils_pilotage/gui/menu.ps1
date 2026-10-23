# Pick items in Win32 popup menus (#32768) by text, using keyboard navigation.
Add-Type @"
using System; using System.Text; using System.Runtime.InteropServices;
public class MN {
  [DllImport("user32.dll")] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] public static extern int GetMenuItemCount(IntPtr m);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetMenuString(IntPtr m, uint id, StringBuilder s, int n, uint f);
  [DllImport("user32.dll")] public static extern uint GetMenuState(IntPtr m, uint id, uint f);
  public static string Item(IntPtr m, int i){ var s=new StringBuilder(512); GetMenuString(m,(uint)i,s,512,0x400); return s.ToString(); }
}
"@
function Menu-Windows($procId){ [IQ]::Tops([uint32]$procId) | Where-Object { [IQ]::Cls($_) -eq '#32768' } }
function Menu-Items($w){ $hm=[MN]::SendMessage($w,0x01E1,[IntPtr]0,[IntPtr]0); $n=[MN]::GetMenuItemCount($hm); 0..($n-1) | % { [MN]::Item($hm,$_) } }
# path: list of item texts (prefix match on text before a tab or ' - '). Last item is activated with Enter.
function Menu-Pick($procId, [string[]]$path){
  # close stray submenus left open (keyboard input goes to the deepest one)
  for($g=0;$g -lt 5 -and @(Menu-Windows $procId).Count -gt 1;$g++){
    $small=@(Menu-Windows $procId) | Sort-Object { [MN]::GetMenuItemCount([MN]::SendMessage($_,0x01E1,[IntPtr]0,[IntPtr]0)) } | Select-Object -First 1
    IQ-Key $small 0x25; Start-Sleep -Milliseconds 300
  }
  $known=@(Menu-Windows $procId)
  $w=$known | Sort-Object { -[MN]::GetMenuItemCount([MN]::SendMessage($_,0x01E1,[IntPtr]0,[IntPtr]0)) } | Select-Object -First 1
  for($k=0;$k -lt $path.Count;$k++){
    $hm=[MN]::SendMessage($w,0x01E1,[IntPtr]0,[IntPtr]0); $n=[MN]::GetMenuItemCount($hm)
    $idx=-1; $sel=0
    for($i=0;$i -lt $n;$i++){
      $t=([MN]::Item($hm,$i)).Replace("&","")
      if($t -eq $path[$k] -or $t.StartsWith($path[$k]+' ') -or $t.StartsWith($path[$k]+"`t")){ $idx=$i; break }
    }
    if($idx -lt 0){ throw "menu item not found: $($path[$k]) in [$((Menu-Items $w) -join ' | ')]" }
    # move the highlight with arrow keys until the target item is highlighted (MF_HILITE = 0x80)
    for($guard=0;$guard -lt 200;$guard++){
      $hi=-1; for($i=0;$i -lt $n;$i++){ if(([MN]::GetMenuState($hm,[uint32]$i,0x400) -band 0x80) -ne 0){ $hi=$i; break } }
      if($hi -eq $idx){ break }
      if($hi -lt 0 -or $hi -lt $idx){ IQ-Key $w 0x28 } else { IQ-Key $w 0x26 }
      Start-Sleep -Milliseconds 50
    }
    if($hi -ne $idx){ throw "could not highlight $($path[$k])" }
    if($k -lt $path.Count-1){
      $before=@{}; foreach($x in @(Menu-Windows $procId)){ $before["$x"]=[MN]::SendMessage($x,0x01E1,[IntPtr]0,[IntPtr]0) }
      IQ-Key $w 0x27; Start-Sleep -Milliseconds 500
      $new=$null
      foreach($x in @(Menu-Windows $procId)){ $hmx=[MN]::SendMessage($x,0x01E1,[IntPtr]0,[IntPtr]0); if(-not $before.ContainsKey("$x") -or $before["$x"] -ne $hmx){ $new=$x } }
      if(-not $new){ throw "submenu did not open for $($path[$k])" }
      $w=$new
    } else { IQ-Key $w 0x0D; Start-Sleep -Milliseconds 700 }
  }
}
