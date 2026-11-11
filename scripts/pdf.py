"""Generate the downloadable PDF from the prerendered report HTML."""
from pathlib import Path
import re, html
from bs4 import BeautifulSoup, NavigableString, Comment
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
soup=BeautifulSoup((ROOT/'.svelte-kit/output/prerendered/pages/index.html').read_text(),'html.parser')
ink=colors.HexColor('#172c3b'); teal=colors.HexColor('#00656b')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Text',fontName='Times-Roman',fontSize=10.7,leading=15.2,spaceAfter=9,textColor=ink,allowWidows=0,allowOrphans=0))
styles.add(ParagraphStyle(name='TitleReport',fontName='Times-Roman',fontSize=28,leading=31,spaceAfter=16,textColor=ink))
styles.add(ParagraphStyle(name='Deck',fontName='Times-Roman',fontSize=13,leading=18,spaceAfter=14,textColor=ink))
styles.add(ParagraphStyle(name='Small',fontName='Helvetica',fontSize=8.4,leading=12,spaceAfter=10,textColor=ink))
styles.add(ParagraphStyle(name='Ref',fontName='Helvetica',fontSize=8.2,leading=11,spaceAfter=5,textColor=ink))
styles.add(ParagraphStyle(name='H2Report',fontName='Times-Bold',fontSize=16,leading=19,spaceBefore=18,spaceAfter=10,keepWithNext=True,textColor=ink))
styles.add(ParagraphStyle(name='H3Report',fontName='Times-Bold',fontSize=12,leading=15,spaceBefore=13,spaceAfter=8,keepWithNext=True,textColor=ink))
styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=8.7,leading=12,textColor=ink))
def inline(e):
    if isinstance(e,Comment): return ""
    if isinstance(e,NavigableString): return html.escape(str(e))
    name=e.name; inner=''.join(inline(c) for c in e.children)
    if name in ('strong','b'):return '<b>'+inner+'</b>'
    if name in ('em','i'):return '<i>'+inner+'</i>'
    if name=='br':return '<br/>'
    if name=='a':
        href=e.get('href','')
        link=f'<a href="{html.escape(href,quote=True)}" color="#00656b">{inner}</a>'
        return '<super>'+link+'</super>' if href.startswith('#source-') else link
    return inner
story=[Paragraph('INDEPENDENT RESEARCH · NOVEMBER 11, 2026',styles['Small'])]
head=soup.select_one('.report-header')
story.append(Paragraph(inline(head.h1),styles['TitleReport']))
story.append(Paragraph(inline(head.select_one('.dek')),styles['Deck']))
story.append(Paragraph(inline(head.select_one('.scope')),styles['Small']))
article=soup.select_one('article')
for e in article.children:
    if not getattr(e,'name',None):continue
    if e.name in ('h2','h3'):story.append(Paragraph(inline(e),styles['H2Report' if e.name=='h2' else 'H3Report']))
    elif e.name=='p':story.append(Paragraph(inline(e),styles['Text']))
    elif e.name=='table':
        rows=[[Paragraph(inline(c),styles['Cell']) for c in row.find_all(['td','th'])] for row in e.find_all('tr')]
        t=Table(rows,colWidths=[145,367],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#d9dedb')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t)
    elif e.name=='section':
        story.append(Paragraph('Sources',styles['H2Report']))
        story.append(Paragraph(inline(e.find('p')),styles['Small']))
        for n,li in enumerate(e.find_all('li'),1):
            title=li.select_one('.source-title'); ps=li.find_all('p')
            text=f'<a name="source-{n}"/><b>{n}. {inline(title)}</b><br/>'+inline(ps[1])+'<br/>'+inline(ps[2])
            story.append(KeepTogether([Paragraph(text,styles['Ref'])]))
def footer(c,d):
    c.saveState(); c.setStrokeColor(colors.HexColor('#d9dedb')); c.line(50,39,562,39)
    c.setFillColor(ink);c.setFont('Helvetica',8);c.drawString(50,27,'FedRAMP monitoring · Independent historical report');c.drawRightString(562,27,str(d.page));c.restoreState()
p=ROOT/'static/fedramp-monitoring-history.pdf'
doc=SimpleDocTemplate(str(p),pagesize=(612,792),leftMargin=50,rightMargin=50,topMargin=46,bottomMargin=52,title='FedRAMP monitoring: from scanner evidence to VDR and VER',author='pwai.dev',pageCompression=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(p); assert len(r.pages)<=15,f'{len(r.pages)} pages exceeds limit'
print(f'PDF: {len(r.pages)} pages, {p.stat().st_size:,} bytes')
