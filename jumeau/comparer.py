"""Compare old logic and v2 in a twin run, and check the scenario expectations.

python -I comparer.py <journal.csv> <paires.csv> <scenario.json> <rapport.md> <E|T>
"""
import csv
import json
import sys


def num(v):
    try:
        return float(v)
    except ValueError:
        return None


def same(a, b, nature):
    if a is None or b is None:
        return a is b
    if nature == 'digital':
        return (a != 0) == (b != 0)
    return abs(a - b) <= max(0.5, 0.01 * max(abs(a), abs(b)))


def main(log_path, pairs_path, scenario_path, out_path, variant):
    with open(log_path, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f, delimiter=';'))
    with open(pairs_path, encoding='utf-8-sig') as f:
        pairs = [p for p in csv.DictReader(f, delimiter=';') if p['variante'] in ('*', variant)]
    with open(scenario_path, encoding='utf-8-sig') as f:
        sc = json.load(f)
    cols = rows[0].keys() if rows else []

    out = [f"# Jumeau : {sc.get('nom', '')}", '',
           f"Profil `{sc['profil']}`, {len(rows)} points, {rows[-1]['t_s'] if rows else 0} s simulees.", '']

    checks = []
    for exp in sc.get('attendus', []):
        canal, t = exp['canal'], float(exp['t'])
        row = next((r for r in rows if float(r['t_s']) >= t - 1e-6), None)
        if row is None or canal not in row:
            checks.append((exp, None, 'non mesure'))
            continue
        v = num(row[canal])
        ok = v is not None and (('egal' in exp and abs(v - exp['egal']) < 1e-6)
                                or ('min' in exp and v >= exp['min'] and ('max' not in exp or v <= exp['max']))
                                or ('max' in exp and 'min' not in exp and v <= exp['max']))
        checks.append((exp, v, 'OK' if ok else 'ECHEC'))
    out += ['## Attendus du scenario', '', '| t (s) | Canal | Attendu | Mesure | Resultat |', '|---|---|---|---|---|']
    for exp, v, res in checks:
        attendu = exp.get('egal', f"{exp.get('min', '')} .. {exp.get('max', '')}")
        out.append(f"| {exp['t']} | {exp['canal']} | {attendu} | {v} | {res} |")

    diffs, sames, missing = [], 0, 0
    for p in pairs:
        if p['v2'] not in cols or p['ancien'] not in cols:
            missing += 1
            continue
        bad = [r for r in rows if not same(num(r[p['v2']]), num(r[p['ancien']]), p['nature'])]
        if bad:
            first = bad[0]
            diffs.append((p, len(bad), first['t_s'], first[p['ancien']], first[p['v2']]))
        else:
            sames += 1
    out += ['', '## Ancienne logique / v2', '',
            f"{sames} paires identiques sur tout le scenario, {len(diffs)} differentes, {missing} non enregistrees.", '']
    if diffs:
        out += ['| Module | v2 | 108.3.1 | Points differents | Premier ecart (s) | 108.3.1 | v2 |', '|---|---|---|---|---|---|---|']
        for p, n, t, a, b in sorted(diffs, key=lambda d: float(d[2])):
            out.append(f"| {p['module']} | {p['v2']} | {p['ancien']} | {n}/{len(rows)} | {t} | {a} | {b} |")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print(f"Rapport : {out_path} ({sum(1 for c in checks if c[2] == 'OK')}/{len(checks)} attendus OK, {len(diffs)} paires differentes)")


if __name__ == '__main__':
    main(*sys.argv[1:6])
