# Cross-process TreeView helpers for the 32-bit IQANdesign (TIQANTreeView = SysTreeView32).
Add-Type @"
using System; using System.Text; using System.Collections.Generic; using System.Runtime.InteropServices;
public class TV {
  [DllImport("user32.dll")] static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("kernel32.dll")] static extern IntPtr OpenProcess(uint a, bool i, uint pid);
  [DllImport("kernel32.dll")] static extern IntPtr VirtualAllocEx(IntPtr p, IntPtr a, uint s, uint t, uint pr);
  [DllImport("kernel32.dll")] static extern bool VirtualFreeEx(IntPtr p, IntPtr a, uint s, uint t);
  [DllImport("kernel32.dll")] static extern bool WriteProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr w);
  [DllImport("kernel32.dll")] static extern bool ReadProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr r);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  public static string Text(IntPtr tv, IntPtr item){
    uint pid; GetWindowThreadProcessId(tv, out pid);
    IntPtr hp = OpenProcess(0x0008|0x0010|0x0020|0x0400, false, pid);
    IntPtr mem = VirtualAllocEx(hp, IntPtr.Zero, 4096, 0x3000, 0x04);
    int textOff = 64; byte[] it = new byte[40];
    BitConverter.GetBytes(0x0001).CopyTo(it,0);                       // TVIF_TEXT
    BitConverter.GetBytes((int)item.ToInt64()).CopyTo(it,4);
    BitConverter.GetBytes((int)(mem.ToInt64()+textOff)).CopyTo(it,16);
    BitConverter.GetBytes(1000).CopyTo(it,20);
    IntPtr w; WriteProcessMemory(hp, mem, it, 40, out w);
    SendMessage(tv, 0x113E, IntPtr.Zero, mem);                        // TVM_GETITEMW
    byte[] buf = new byte[2000]; IntPtr r; ReadProcessMemory(hp, new IntPtr(mem.ToInt64()+textOff), buf, 2000, out r);
    VirtualFreeEx(hp, mem, 0, 0x8000); CloseHandle(hp);
    string s = Encoding.Unicode.GetString(buf); int z = s.IndexOf('\0'); return z>=0 ? s.Substring(0,z) : s;
  }
  public static IntPtr Next(IntPtr tv, IntPtr item, int code){ return SendMessage(tv, 0x110A, new IntPtr(code), item); }
  public static List<IntPtr> Children(IntPtr tv, IntPtr item){
    var r = new List<IntPtr>(); IntPtr c = item==IntPtr.Zero ? Next(tv, IntPtr.Zero, 0) : Next(tv, item, 4);
    while(c != IntPtr.Zero){ r.Add(c); c = Next(tv, c, 1); } return r;
  }
  public static void Expand(IntPtr tv, IntPtr item){ SendMessage(tv, 0x1102, new IntPtr(2), item); }
  public static void Select(IntPtr tv, IntPtr item){ SendMessage(tv, 0x110B, new IntPtr(9), item); }
  public static void Visible(IntPtr tv, IntPtr item){ SendMessage(tv, 0x1114, IntPtr.Zero, item); }
}
"@
function TV-Find($tv, [string[]]$path){
  $cur=[IntPtr]::Zero
  foreach($p in $path){
    if($cur -ne [IntPtr]::Zero){ [TV]::Expand($tv,$cur); Start-Sleep -Milliseconds 300 }
    $hit=$null
    foreach($c in [TV]::Children($tv,$cur)){ $t=[TV]::Text($tv,$c); if($t -eq $p -or $t -like "$p (*"){ $hit=$c; break } }
    if(-not $hit){ throw "not found: $p under $([TV]::Text($tv,$cur))" }
    $cur=$hit
  }
  return $cur
}
function TV-Dump($tv,$item,$depth=0,$max=1){
  foreach($c in [TV]::Children($tv,$item)){ ('  '*$depth)+[TV]::Text($tv,$c); if($depth -lt $max){ TV-Dump $tv $c ($depth+1) $max } }
}
