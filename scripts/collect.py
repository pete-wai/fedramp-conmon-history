"""Capture public sources or copy selected inforegs records without modifying archive."""
import hashlib, json, sys, io, concurrent.futures, zipfile
from pathlib import Path
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from pypdf import PdfReader
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
(ROOT/'research/raw').mkdir(parents=True, exist_ok=True)
(ROOT/'research/text').mkdir(parents=True, exist_ok=True)
def capture(item):
    ident, url = item['id'], item['url']
    try:
        if item.get('local'):
            data = Path(item['local']).read_bytes(); resolved = url
        else:
            r = requests.get(url, timeout=45); r.raise_for_status(); data=r.content; resolved=r.url
        ext = 'pdf' if data.startswith(b'%PDF') else 'xlsx' if data.startswith(b'PK') and ('xlsx' in url or 'xlsm' in url) else 'docx' if data.startswith(b'PK') and 'docx' in url else 'html' if b'<html' in data[:2000].lower() else 'txt'
        path=ROOT/'research/raw'/f'{ident}.{ext}'; path.write_bytes(data)
        if ext=='pdf':
            reader=PdfReader(io.BytesIO(data)); content='\n\n'.join(f'--- PDF page {i+1} ---\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages)); item['pages']=len(reader.pages)
        elif ext=='xlsx':
            wb=load_workbook(io.BytesIO(data),data_only=False); content='\n\n'.join('SHEET: '+s.title+'\n'+'\n'.join(' | '.join(str(v) if v is not None else '' for v in row) for row in s.values if any(v is not None for v in row)) for s in wb)
        elif ext=='docx':
            with zipfile.ZipFile(io.BytesIO(data)) as z: content='\n'.join(''.join(e.itertext()) for e in ET.fromstring(z.read('word/document.xml')).iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
        elif ext=='html':
            soup=BeautifulSoup(data,'html.parser')
            for e in soup(['script','style','nav','footer','header']): e.decompose()
            content=(soup.find('main') or soup).get_text('\n',strip=True)
        else: content=data.decode('utf-8',errors='replace')
        (ROOT/'research/text'/f'{ident}.txt').write_text(content)
        item.update(status='retrieved',resolved_url=resolved,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),characters=len(content),retrieved_at='2026-11-11')
    except Exception as e: item.update(status='failed',error=str(e))
    print(ident,item['status'],item.get('characters',item.get('error')))
    return item
if __name__=='__main__':
    items=json.loads(Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(capture,items))
    (ROOT/'research'/f'{Path(sys.argv[1]).stem}-receipt.json').write_text(json.dumps(results,indent=2))
