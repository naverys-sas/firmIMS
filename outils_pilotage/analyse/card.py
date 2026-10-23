"""Print the knowledge-base card(s) of one or more channels by exact name.

Usage: python -I card.py kb_dir "Channel name" ["Other name" ...]
"""
import glob, os, sys

kb, names = sys.argv[1], sys.argv[2:]
sys.stdout.reconfigure(encoding='utf-8')
for path in glob.glob(os.path.join(kb, 'fonctions', '*.md')):
    lines = open(path, encoding='utf-8').read().split('\n')
    for i, l in enumerate(lines):
        if l.startswith('#### ') and l[5:].rsplit('  `', 1)[0] in names:
            j = i + 1
            while j < len(lines) and not lines[j].startswith('#') :
                j += 1
            print(f"[{os.path.basename(path)}]")
            print('\n'.join(lines[i:j]))
