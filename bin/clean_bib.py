#!/usr/bin/env python3
"""Clean a DBLP/Scholar BibTeX export into an al-folio papers.bib.
Usage: python3 bin/clean_bib.py in1.bib [in2.bib ...] -o _bibliography/papers.bib"""
import re, sys, io, collections

ABBR = [
 (r'Nature Medicine|Nat\. Med', 'Nat. Med.'),
 (r'\bNeurIPS\b|Neural Information Processing Systems', 'NeurIPS'),
 (r'International Conference on Learning Representations|\bICLR\b', 'ICLR'),
 (r'International Conference on Machine Learning|\bICML\b', 'ICML'),
 (r'Association for Computational Linguistics|\bACL\b', 'ACL'),
 (r'Empirical Methods in Natural Language|\bEMNLP\b', 'EMNLP'),
 (r'\bMICCAI\b|Medical Image Computing', 'MICCAI'),
 (r'\bISBI\b|Biomedical Imaging', 'ISBI'),
 (r'\bCVPR\b|Computer Vision and Pattern Recognition', 'CVPR'),
 (r'\bICCV\b'  , 'ICCV'), (r'\bECCV\b', 'ECCV'),
 (r'\bAAAI\b', 'AAAI'), (r'\bKDD\b', 'KDD'), (r'\bBIBM\b', 'BIBM'),
 (r'\bAMIA\b', 'AMIA'), (r'ACM Multimedia|ACM MM', 'ACM MM'),
 (r'Trans\.? on Medical Imaging|Trans\. Med\. Imaging', 'IEEE TMI'),
 (r'J\.? Biomed\.? Health Informatics', 'IEEE JBHI'),
 (r'Trans\.? Biomed\.? Eng', 'IEEE TBME'),
 (r'Trans\.? Neural Networks', 'IEEE TNNLS'),
 (r'Trans\.? Big Data', 'IEEE TBD'),
 (r'Medical Image Anal', 'MedIA'),
 (r'Nuclear Medicine', 'JNM'),
 (r'Medical Physics', 'Med. Phys.'),
 (r'^CoRR$|arXiv', 'arXiv'),
]
DROP_FIELDS = {'timestamp','biburl','bibsource','ee'}

def field(e, k):
    """Brace-balanced field extraction: handles nested {IEEE} inside values."""
    m = re.search(r'\n\s*' + k + r'\s*=\s*\{', e, re.I)
    if not m: return ''
    i = m.end(); depth = 1; out = []
    while i < len(e) and depth:
        c = e[i]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if not depth: break
        out.append(c); i += 1
    return re.sub(r'\s+', ' ', ''.join(out)).strip()

def parse(text):
    return re.findall(r'(@\w+\{[^@]*?\n\})', text, re.S)

def norm(t):
    return re.sub(r'[^a-z0-9]','',t.lower())

def abbr_for(venue):
    for pat, ab in ABBR:
        if re.search(pat, venue, re.I): return ab
    return ''

def mkkey(authors, year, title, taken):
    last = 'anon'
    if authors:
        first = authors.split(' and ')[0].strip()
        last = (first.split(',')[0] if ',' in first else first.split()[-1])
    last = re.sub(r'[^A-Za-z]','',last).lower() or 'anon'
    word = next((w for w in re.sub(r'[^a-zA-Z ]','',title).split()
                 if len(w) > 3 and w.lower() not in
                 {'with','from','using','this','that','their','into','more','over'}), 'paper')
    base = f"{last}{year or 'nd'}{word.lower()}"
    k, i = base, 1
    while k in taken: i += 1; k = f"{base}{i}"
    taken.add(k); return k

def main():
    args = sys.argv[1:]
    out = '_bibliography/papers.bib'
    if '-o' in args:
        i = args.index('-o'); out = args[i+1]; args = args[:i] + args[i+2:]
    raw = []
    for p in args:
        raw += parse(io.open(p, encoding='utf-8', errors='replace').read())
    recs = []
    for e in raw:
        t = re.match(r'@(\w+)', e).group(1).lower()
        rec = dict(type=t, raw=e, title=field(e,'title'), year=field(e,'year'),
                   author=field(e,'author') or field(e,'editor'),
                   venue=field(e,'journal') or field(e,'booktitle') or field(e,'school'),
                   doi=field(e,'doi'), url=field(e,'url'))
        rec['n'] = norm(rec['title']); rec['pre'] = bool(re.search(r'^CoRR$|arxiv', rec['venue'], re.I))
        recs.append(rec)

    report = collections.Counter()
    published = {r['n'] for r in recs if not r['pre'] and r['n']}
    kept, seen = [], {}
    for r in recs:
        if r['type'] == 'proceedings':
            report['dropped: edited volume'] += 1; continue
        if not r['title']:
            report['dropped: no title'] += 1; continue
        if r['pre'] and r['n'] in published:
            report['dropped: preprint superseded by published version'] += 1; continue
        if r['n'] in seen:
            prev = seen[r['n']]
            if prev['pre'] and not r['pre']:
                kept[kept.index(prev)] = r; seen[r['n']] = r
                report['deduped: kept published over preprint'] += 1
            else:
                report['dropped: duplicate title'] += 1
            continue
        seen[r['n']] = r; kept.append(r)

    kept.sort(key=lambda r: (-(int(r['year']) if r['year'].isdigit() else 0), r['title']))
    taken = set(); lines = ['---', '---', '']
    for r in kept:
        key = mkkey(r['author'], r['year'], r['title'], taken)
        et = {'inproceedings':'inproceedings','article':'article',
              'phdthesis':'phdthesis'}.get(r['type'], r['type'])
        vkey = 'booktitle' if et == 'inproceedings' else ('school' if et=='phdthesis' else 'journal')
        body = [f'@{et}{{{key},',
                f'  title     = {{{r["title"]}}},',
                f'  author    = {{{r["author"]}}},']
        if r['venue']: body.append(f'  {vkey:9s} = {{{r["venue"]}}},')
        if r['year']:  body.append(f'  year      = {{{r["year"]}}},')
        if r['doi']:   body.append(f'  doi       = {{{r["doi"]}}},')
        if r['url']:   body.append(f'  url       = {{{r["url"]}}},')
        ab = abbr_for(r['venue'])
        if ab:         body.append(f'  abbr      = {{{ab}}},')
        body.append('  bibtex_show = {true}')
        body.append('}\n')
        lines += body
    io.open(out,'w',encoding='utf-8').write('\n'.join(lines))
    print(f"input entries : {len(recs)}")
    for k,v in sorted(report.items()): print(f"  {k}: {v}")
    print(f"WROTE {len(kept)} entries -> {out}")
    pre = sum(1 for r in kept if r['pre'])
    print(f"  of which arXiv-only (no published version found): {pre}")

main()
