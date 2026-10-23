"""Extract 'MC42 cavity -> harness signal' pairs from a RapidHarness PDF text export (pdftotext -layout).

Two patterns appear in these drawings:
  "<cavity> <Signal>.<pin> W<n>.<Color>"   (rows of the Main_MC42 connector table)
  "<Signal>.<pin> Main_MC42.<cavity> W<n>" (rows of the other connectors / wiring table)
Usage: python -I harness_pins.py file.txt [file2.txt ...]  -> prints cavity;signal lines per file
"""
import re, sys
from collections import defaultdict

A = re.compile(r'(?:^|\s)(\d{1,2})\s+([A-Za-z][\w\-]*(?:\.[A-Z0-9]+)?)\s+W\d+\.')
B = re.compile(r'([A-Za-z][\w\-]*(?:\.[A-Z0-9]+)?)\s+Main_MC42\.(\d{1,2})\s+W\d+')
C = re.compile(r'Main_MC42\.(\d{1,2})\s+([A-Za-z][\w\-]*(?:\.[A-Z0-9]+)?)\s+W\d+')


def parse(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    pins = defaultdict(set)
    in_main = False
    for line in txt.split('\n'):
        for m in B.finditer(line):
            if not m.group(1).startswith('Main_MC42'):
                pins[int(m.group(2))].add(m.group(1).split('.')[0])
        for m in C.finditer(line):
            pins[int(m.group(1))].add(m.group(2).split('.')[0])
    # Main_MC42 table rows: lines starting with the cavity number
    for line in txt.split('\n'):
        m = re.match(r'^\s?(\d{1,2})\s+([A-Za-z][\w\-]*)(?:\.[A-Z0-9]+)?\s+W\d+\.', line)
        if m and 1 <= int(m.group(1)) <= 66:
            pins[int(m.group(1))].add(m.group(2))
    return pins


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print('###', p)
        for k, v in sorted(parse(p).items()):
            print(f"C1:{k};{', '.join(sorted(v))}")
