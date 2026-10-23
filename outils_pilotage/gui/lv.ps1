# Read a SysListView32 (TListView) of the 32-bit IQANdesign cross-process.
Add-Type @"
using System; using System.Text; using System.Runtime.InteropServices;
public class LV {
  [DllImport("user32.dll")] static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("kernel32.dll")] static extern IntPtr OpenProcess(uint a, bool i, uint pid);
  [DllImport("kernel32.dll")] static extern IntPtr VirtualAllocEx(IntPtr p, IntPtr a, uint s, uint t, uint pr);
  [DllImport("kernel32.dll")] static extern bool VirtualFreeEx(IntPtr p, IntPtr a, uint s, uint t);
  [DllImport("kernel32.dll")] static extern bool WriteProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr w);
  [DllImport("kernel32.dll")] static extern bool ReadProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr r);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  public static int Count(IntPtr lv){ return (int)SendMessage(lv, 0x1004, IntPtr.Zero, IntPtr.Zero); }
  public static string Cell(IntPtr lv, int item, int sub){
    uint pid; GetWindowThreadProcessId(lv, out pid);
    IntPtr hp = OpenProcess(0x0008|0x0010|0x0020|0x0400, false, pid);
    IntPtr mem = VirtualAllocEx(hp, IntPtr.Zero, 4096, 0x3000, 0x04);
    byte[] it = new byte[60];
    BitConverter.GetBytes(0x0001).CopyTo(it,0); BitConverter.GetBytes(item).CopyTo(it,4); BitConverter.GetBytes(sub).CopyTo(it,8);
    BitConverter.GetBytes((int)(mem.ToInt64()+64)).CopyTo(it,20); BitConverter.GetBytes(1000).CopyTo(it,24);
    IntPtr w; WriteProcessMemory(hp, mem, it, 60, out w);
    SendMessage(lv, 0x1073, new IntPtr(item), mem);
    byte[] buf = new byte[2000]; IntPtr r; ReadProcessMemory(hp, new IntPtr(mem.ToInt64()+64), buf, 2000, out r);
    VirtualFreeEx(hp, mem, 0, 0x8000); CloseHandle(hp);
    string s = Encoding.Unicode.GetString(buf); int z = s.IndexOf('\0'); return z>=0 ? s.Substring(0,z) : s;
  }
}
"@
function LV-Dump($lv,$cols=4){ $n=[LV]::Count($lv); for($i=0;$i -lt $n;$i++){ (0..($cols-1) | % { [LV]::Cell($lv,$i,$_) }) -join "`t" } }
