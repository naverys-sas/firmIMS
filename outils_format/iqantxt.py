"""Lecture d'un export texte IQANdesign (-saveas x.txt) en objets {id: (classe, propriétés, parent)}."""
import re

_begin = re.compile(r"^\s*BEGIN (\d+)\s*$")
_end = re.compile(r"^\s*END (\d+)\s*$")


def read(path):
    raw = open(path, "rb").read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    lines = text.splitlines()
    objs, stack, i = {}, [], 0
    while i < len(lines):
        ln = lines[i]
        m = _begin.match(ln)
        if m:
            oid = int(m.group(1))
            cls = lines[i + 1].strip()
            parent = stack[-1] if stack else None
            objs[oid] = {"id": oid, "cls": cls, "props": [], "parent": parent, "children": []}
            if parent is not None:
                objs[parent]["children"].append(oid)
            stack.append(oid)
            i += 2
            continue
        m = _end.match(ln)
        if m:
            stack.pop()
        elif stack and "=" in ln and not ln.startswith("  " * (len(stack) - 1) + "  " * 1 + " "):
            k, _, v = ln.strip().partition("=")
            objs[stack[-1]]["props"].append((k, v))
        i += 1
    return objs
