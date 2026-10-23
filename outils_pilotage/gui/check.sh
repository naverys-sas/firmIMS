#!/bin/sh
# Export a copy of the v2 working project and diff it against the 108.3.1 export (logic level + raw).
set -e
S=/c/Users/Sav78/Documents/testia_sandbox
cp "$S/v2_mc42/v2_mc42.idax" "$S/v2_check/chk.idax"
rm -f "$S/v2_check/chk.txt"
powershell.exe -NoProfile -Command "\$p=Start-Process -FilePath 'C:\Program Files (x86)\IQANdesign 6.08\IQANdesign.exe' -ArgumentList '\"C:\Users\Sav78\Documents\testia_sandbox\v2_check\chk.idax\" -saveas \"C:\Users\Sav78\Documents\testia_sandbox\v2_check\chk.txt\"' -PassThru; \$p.WaitForExit(60000) | Out-Null"
python -I "$S/v117/tools/diff_versions.py" "$S/v1083/v1083.txt" "$S/v2_check/chk.txt" "$S/v2_check/diff.md" "108.3.1" "v2 en cours"
python -I "$S/v117/tools/compat_check.py" "$S/v1083/v1083.txt" "$S/v2_check/chk.txt" "$S/v2_check/compat.md"
