# Real-mouse helpers (move the user's cursor): only with the user's consent, while they leave the PC alone.
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Threading;
public class RM {
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, int dx, int dy, uint d, IntPtr e);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int c);
  [DllImport("user32.dll")] public static extern void keybd_event(byte k, byte s, uint f, IntPtr e);
  [DllImport("user32.dll")] static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] static extern bool ClientToScreen(IntPtr h, ref int[] p);
  [DllImport("user32.dll")] static extern bool MapWindowPoints(IntPtr f, IntPtr t, int[] p, int n);
  [DllImport("kernel32.dll")] static extern IntPtr OpenProcess(uint a, bool i, uint pid);
  [DllImport("kernel32.dll")] static extern IntPtr VirtualAllocEx(IntPtr p, IntPtr a, uint s, uint t, uint pr);
  [DllImport("kernel32.dll")] static extern bool VirtualFreeEx(IntPtr p, IntPtr a, uint s, uint t);
  [DllImport("kernel32.dll")] static extern bool WriteProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr w);
  [DllImport("kernel32.dll")] static extern bool ReadProcessMemory(IntPtr p, IntPtr a, byte[] b, uint s, out IntPtr r);
  [DllImport("kernel32.dll")] static extern bool CloseHandle(IntPtr h);
  public static void Front(IntPtr h){ keybd_event(0x12,0,0,IntPtr.Zero); keybd_event(0x12,0,2,IntPtr.Zero); ShowWindow(h,3); SetForegroundWindow(h); }
  // screen rect (l,t,r,b) of a tree item's text
  public static int[] ItemRect(IntPtr tv, IntPtr item){
    uint pid; GetWindowThreadProcessId(tv, out pid);
    IntPtr hp = OpenProcess(0x0008|0x0010|0x0020|0x0400, false, pid);
    IntPtr mem = VirtualAllocEx(hp, IntPtr.Zero, 64, 0x3000, 0x04);
    IntPtr w; WriteProcessMemory(hp, mem, BitConverter.GetBytes((int)item.ToInt64()), 4, out w);
    SendMessage(tv, 0x1104, new IntPtr(1), mem);
    byte[] b = new byte[16]; IntPtr r; ReadProcessMemory(hp, mem, b, 16, out r);
    VirtualFreeEx(hp, mem, 0, 0x8000); CloseHandle(hp);
    int[] p = { BitConverter.ToInt32(b,0), BitConverter.ToInt32(b,4), BitConverter.ToInt32(b,8), BitConverter.ToInt32(b,12) };
    MapWindowPoints(tv, IntPtr.Zero, p, 2); return p;
  }
  public static void Drag(int x1, int y1, int x2, int y2){
    SetCursorPos(x1,y1); Thread.Sleep(300);
    mouse_event(0x2,0,0,0,IntPtr.Zero); Thread.Sleep(300);
    for(int i=1;i<=30;i++){ SetCursorPos(x1+(x2-x1)*i/30, y1+(y2-y1)*i/30); Thread.Sleep(40); }
    Thread.Sleep(600); mouse_event(0x4,0,0,0,IntPtr.Zero); Thread.Sleep(500);
  }
}
"@
