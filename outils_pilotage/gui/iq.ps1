# Helpers to drive IQANdesign by window messages (no real mouse/keyboard).
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System; using System.Text; using System.Collections.Generic; using System.Runtime.InteropServices;
public class IQ {
  public delegate bool P(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] static extern bool EnumWindows(P p, IntPtr l);
  [DllImport("user32.dll")] static extern bool EnumChildWindows(IntPtr w, P p, IntPtr l);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr dc, uint f);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr PostMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, string l);
  [DllImport("user32.dll")] public static extern bool ScreenToClient(IntPtr h, ref POINT p);
  public struct RECT { public int L,T,R,B; }
  public struct POINT { public int X,Y; }
  public static List<IntPtr> Tops(uint id){ var r=new List<IntPtr>(); EnumWindows((h,l)=>{uint p; GetWindowThreadProcessId(h,out p); if(p==id && IsWindowVisible(h)) r.Add(h); return true;},IntPtr.Zero); return r; }
  public static List<IntPtr> Kids(IntPtr w){ var r=new List<IntPtr>(); EnumChildWindows(w,(h,l)=>{r.Add(h);return true;},IntPtr.Zero); return r; }
  public static string Txt(IntPtr h){ var s=new StringBuilder(512); GetWindowText(h,s,512); return s.ToString(); }
  public static string Cls(IntPtr h){ var s=new StringBuilder(256); GetClassName(h,s,256); return s.ToString(); }
}
"@
[IQ]::SetProcessDPIAware() | Out-Null
function IQ-Proc { Get-Process IQANdesign | Where-Object { $_.MainWindowTitle -like '*v2_mc42*' -or $_.MainWindowTitle -like '*v2_mc2*' } | Select-Object -First 1 }
function IQ-List($proc){ foreach($t in [IQ]::Tops([uint32]$proc.Id)){ $r=New-Object IQ+RECT; [IQ]::GetWindowRect($t,[ref]$r)|Out-Null; "TOP $t | $([IQ]::Cls($t)) | $([IQ]::Txt($t)) | $($r.L),$($r.T),$($r.R),$($r.B)" } }
function IQ-Kids($h,[switch]$visible){ foreach($k in [IQ]::Kids([IntPtr]$h)){ if($visible -and -not [IQ]::IsWindowVisible($k)){continue}; $r=New-Object IQ+RECT; [IQ]::GetWindowRect($k,[ref]$r)|Out-Null; "$k | $([IQ]::Cls($k)) | $([IQ]::Txt($k)) | $($r.L),$($r.T),$($r.R),$($r.B)" } }
function IQ-Shot($h,$path){ $r=New-Object IQ+RECT; [IQ]::GetWindowRect([IntPtr]$h,[ref]$r)|Out-Null; $b=New-Object Drawing.Bitmap ([Math]::Max(1,$r.R-$r.L)),([Math]::Max(1,$r.B-$r.T)); $g=[Drawing.Graphics]::FromImage($b); $dc=$g.GetHdc(); [IQ]::PrintWindow([IntPtr]$h,$dc,2)|Out-Null; $g.ReleaseHdc($dc); $b.Save($path); "$($r.L),$($r.T) $($b.Width)x$($b.Height)" }
function MkL($x,$y){ [IntPtr](($y -shl 16) -bor ($x -band 0xFFFF)) }
function IQ-Click($h,$x,$y){ [IQ]::PostMessage([IntPtr]$h,0x201,[IntPtr]1,(MkL $x $y))|Out-Null; Start-Sleep -Milliseconds 60; [IQ]::PostMessage([IntPtr]$h,0x202,[IntPtr]0,(MkL $x $y))|Out-Null }
function IQ-DblClick($h,$x,$y){ IQ-Click $h $x $y; Start-Sleep -Milliseconds 80; [IQ]::PostMessage([IntPtr]$h,0x203,[IntPtr]1,(MkL $x $y))|Out-Null; Start-Sleep -Milliseconds 60; [IQ]::PostMessage([IntPtr]$h,0x202,[IntPtr]0,(MkL $x $y))|Out-Null }
function IQ-RClick($h,$x,$y){ [IQ]::PostMessage([IntPtr]$h,0x204,[IntPtr]2,(MkL $x $y))|Out-Null; Start-Sleep -Milliseconds 60; [IQ]::PostMessage([IntPtr]$h,0x205,[IntPtr]0,(MkL $x $y))|Out-Null }
function IQ-Key($h,$vk){ [IQ]::PostMessage([IntPtr]$h,0x100,[IntPtr]$vk,[IntPtr]0)|Out-Null; Start-Sleep -Milliseconds 40; [IQ]::PostMessage([IntPtr]$h,0x101,[IntPtr]$vk,[IntPtr]0)|Out-Null }
function IQ-Chars($h,$s){ foreach($c in $s.ToCharArray()){ [IQ]::PostMessage([IntPtr]$h,0x102,[IntPtr][int]$c,[IntPtr]0)|Out-Null; Start-Sleep -Milliseconds 15 } }
