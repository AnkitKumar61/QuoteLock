"""Check release-local Markdown links and excluded runtime artefacts."""
from pathlib import Path
import re,sys,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent.parent
def main():
 errors=[];links=0
 for file in [ROOT/'README.md',*(ROOT/'docs').rglob('*.md'),ROOT/'CONTRIBUTING.md',ROOT/'NOTICE.md',ROOT/'SECURITY.md']:
  text=file.read_text(encoding='utf-8')
  candidates=re.findall(r'\]\(([^)]+)\)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
  for url in candidates:
   if re.match(r'^(?:https?:|mailto:|#)',url):continue
   path=url.split('#')[0].split('?')[0].strip('<>')
   if path:
    links+=1
    if not (file.parent/path).exists():errors.append(str(file.relative_to(ROOT))+': '+url)
 allowed_pdf='docs/presentation/QuoteLock_Logging_Final_v2.pdf'
 expected_pdf_hash='9411dafcd9c764b4cd88ed1c75b388039216ca055331319e004c3006f0dec1f8'
 for suffix in ['*.pptx','*.pdf','*.exe','*.dll','*.pem','*.key']:
  for p in ROOT.rglob(suffix):
   if any(x in p.parts for x in ['.venv','.git','__pycache__']):continue
   relative=p.relative_to(ROOT).as_posix()
   if relative==allowed_pdf:
    if hashlib.sha256(p.read_bytes()).hexdigest()!=expected_pdf_hash:errors.append('Supplied presentation changed: '+relative)
   else:errors.append('Unexpected release file: '+relative)
 diagram=ET.parse(ROOT/'docs/architecture/quotelock-system.drawio')
 cells=diagram.findall('.//mxCell')
 core={(c.get('source'),c.get('target')) for c in cells if c.get('data-core')=='true'}
 contract=json.loads((ROOT/'quotelock/architecture.json').read_text(encoding='utf-8'))
 if core!={(a,b) for a,b,_ in contract['edges']}:errors.append('Architecture core paths differ from implementation contract')
 model=diagram.find('.//mxCell[@id="A2"]')
 if model is None or model.get('parent')!='boundary':errors.append('A2 must be the only model-boundary module')
 if {c.get('id') for c in cells if c.get('parent')=='boundary' and c.get('id') in ['A1','A2','A3','A4','A5','A6']}!={'A2'}:errors.append('Other modules entered the model boundary')
 ET.parse(ROOT/'docs/architecture/quotelock-system.svg')
 print(json.dumps({'local_links_checked':links,'architecture_core_paths':len(core),'errors':errors},indent=2))
 return bool(errors)
if __name__=='__main__':sys.exit(main())
