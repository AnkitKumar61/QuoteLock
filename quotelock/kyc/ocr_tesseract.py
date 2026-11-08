from pathlib import Path
import subprocess,json,time,cv2,numpy as np,hashlib,re,os,shutil
from quotelock.kyc import parse_ocr
ROOT=Path(__file__).resolve().parents[2]
def engine_path():
 configured=os.environ.get('TESSERACT_CMD')
 if configured:
  p=Path(configured).expanduser()
  if p.is_file():return str(p)
  raise RuntimeError('TESSERACT_CMD must point to an installed Tesseract executable')
 found=shutil.which('tesseract')
 if found:return found
 raise RuntimeError('Fresh OCR requires Tesseract with English data on PATH or TESSERACT_CMD; recorded source packets work without it')
def image_ocr(path):
 executable=Path(engine_path());data=executable.parent/'tessdata'
 args=[str(executable),str(path),'stdout']
 if data.is_dir():args+=['--tessdata-dir',str(data)]
 p=subprocess.run(args+['-l','eng','--psm','6'],capture_output=True,timeout=25)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace')[:300])
 lines=[s.strip() for s in p.stdout.decode('utf-8',errors='replace').splitlines() if s.strip()]
 return {'text':' '.join(lines),'lines':lines}
def fields_from_documents(docs):
 # Label-anchored whole-page extraction preserves wrapped value text. The
 # initial column crop clipped left-hand glyphs and is not used for decisions.
 full={k:{**v,'text':v.get('full_text',v['text'])} for k,v in docs.items()}
 f=parse_ocr(full)
 def labelled(kind,label,end):
  t=docs.get(kind,{}).get('full_text',docs.get(kind,{}).get('text',''))
  m=re.search(label+r'\s*[:.]?\s*(.*?)\s*'+end,t,re.I)
  return m.group(1).strip() if m else None
 # Signatory layout is interleaved; process labelled full-page text, not the
 # value-column layout used by registration certificates.
 sig=labelled('signatory_id',r'\bName',r'Designation')
 if sig:f['signatory']=sig
 legal=labelled('gst_certificate',r'Legal\s+name',r'Trade\s+name')
 if legal:f['legal']=legal
 gst=labelled('gst_certificate',r'\bGSTIN',r'Legal\s+name')
 f['gstin']=re.sub(r'\s+','',gst).upper() if gst else None
 raw=full.get('udyam_certificate',{}).get('text','')
 u=re.search(r'UDYAM\s*-\s*[A-Z]{2}\s*-\s*[0-9]{2}\s*-\s*[0-9]{7}',raw,re.I)
 f['udyam']=re.sub(r'\s+','',u.group(0)).upper() if u else None
 address=labelled('gst_certificate',r'Address\s+of\s+principal',r'Date\s+of\s+liability')
 f['address']=re.sub(r'place\s+of\s+business',' ',address,flags=re.I).strip() if address else None
 return f
def main():
 meta=json.loads((ROOT/'evaluation/ocr_preprocessing.json').read_text());dest=ROOT/'quotelock/.data/ocr_images';records=[];beg=time.perf_counter()
 version=subprocess.run([engine_path(),'--version'],capture_output=True,text=True,timeout=10).stdout.splitlines()[0]
 for i,p in enumerate(sorted(p for p in dest.glob('K*.png') if '_value' not in p.stem)):
  full=image_ocr(p);values=full
  records.append({'file':p.name,'engine':version+' eng psm6','source_sha256':meta[p.name]['source_sha256'],'full_text':full['text'],**values,**meta[p.name]})
  if i%10==0:print('OCR completed',i+1,flush=True)
 packets={}
 for r in records:
  packet=r['file'][:3];kind=r['file'][4:-4];packets.setdefault(packet,{})[kind]=r
 result={k:fields_from_documents(d) for k,d in packets.items()}
 (ROOT/'evaluation/ocr_tesseract_raw.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
 (ROOT/'evaluation/ocr_fields.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 (ROOT/'evaluation/ocr_runtime.json').write_text(json.dumps({'engine':version,'documents':len(records),'elapsed_seconds':time.perf_counter()-beg,'method':'OpenCV deskew, whole-page OCR and specimen-label parser; no registry or fixture used in extraction'},indent=2),encoding='utf-8')
 print('Saved fresh extraction for',len(records),'documents')
if __name__=='__main__':main()
