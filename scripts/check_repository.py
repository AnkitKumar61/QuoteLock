"""Check release-local Markdown links and excluded runtime artefacts."""
from pathlib import Path
import re,sys,json
ROOT=Path(__file__).resolve().parent.parent
def main():
 errors=[];links=0
 for file in [ROOT/'README.md',*(ROOT/'docs').glob('*.md'),ROOT/'CONTRIBUTING.md',ROOT/'NOTICE.md',ROOT/'SECURITY.md']:
  text=file.read_text(encoding='utf-8')
  candidates=re.findall(r'\]\(([^)]+)\)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
  for url in candidates:
   if re.match(r'^(?:https?:|mailto:|#)',url):continue
   path=url.split('#')[0].split('?')[0].strip('<>')
   if path:
    links+=1
    if not (file.parent/path).exists():errors.append(str(file.relative_to(ROOT))+': '+url)
 for suffix in ['*.pptx','*.pdf','*.exe','*.dll','*.pem','*.key']:
  for p in ROOT.rglob(suffix):
   if any(x in p.parts for x in ['.venv','.git','__pycache__']):continue
   errors.append('Unexpected release file: '+str(p.relative_to(ROOT)))
 print(json.dumps({'local_links_checked':links,'errors':errors},indent=2))
 return bool(errors)
if __name__=='__main__':sys.exit(main())
