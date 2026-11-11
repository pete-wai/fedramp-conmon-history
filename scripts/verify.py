"""Check PDF completeness and retained evidence without network access."""
from pathlib import Path
import hashlib, json, re
from bs4 import BeautifulSoup
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
r=PdfReader(R/'static/fedramp-monitoring-history.pdf')
assert 1<=len(r.pages)<=15
normalize=lambda s: re.sub(r'\s+','',s).replace('\u00ad','')
pdf=normalize(''.join(re.sub(r'FedRAMP monitoring · Independent historical report\s*\d+', '', p.extract_text()) for p in r.pages))
s=BeautifulSoup((R/'build/index.html').read_text(),'html.parser')
for p in s.select('article > p, article > h2, article > h3, article td, .sources li'):
    txt=normalize(p.get_text())
    # PDF bibliography adds visible source numbers; all authored content must remain present.
    assert txt in pdf,txt[:100]
for item in json.loads((R/'research/source-inventory.json').read_text()):
    if item.get('retained_copy'):
        p=R/item['retained_copy']; assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['id']
assert (R/'build/fedramp-monitoring-history.pdf').read_bytes()==(R/'static/fedramp-monitoring-history.pdf').read_bytes()
print(f'PASS: {len(r.pages)} PDF pages; full narrative, table and bibliography match HTML; retained source hashes match.')
