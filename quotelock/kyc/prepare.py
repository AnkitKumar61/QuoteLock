"""Prepare derivatives only; originals and committed team labels stay untouched."""
from pathlib import Path
import json,cv2,numpy as np,hashlib
ROOT=Path(__file__).resolve().parents[2]
def prepare():
 dest=ROOT/'quotelock/.data/ocr_images';dest.mkdir(parents=True,exist_ok=True);meta={}
 for p in sorted((ROOT/'YTL_TrackA_Udyam_Digital_Data/kyc_documents').glob('*.png')):
  im=cv2.imread(str(p));g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);blur=float(cv2.Laplacian(g,cv2.CV_64F).var())
  _,b=cv2.threshold(g,180,255,cv2.THRESH_BINARY_INV);ys,xs=np.where(b>0);angle=cv2.minAreaRect(np.column_stack((xs,ys)).astype('float32'))[-1]
  angle=angle+90 if angle<-45 else angle
  if abs(angle)>.3 and abs(angle)<15:
   h,w=g.shape;im=cv2.warpAffine(im,cv2.getRotationMatrix2D((w/2,h/2),angle,1),(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_CONSTANT,borderValue=(255,255,255))
  cv2.imwrite(str(dest/p.name),im)
  meta[p.name]={'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'deskew_degrees':float(angle),'blur_variance':blur}
 (ROOT/'evaluation/ocr_preprocessing.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
 print('Prepared',len(meta),'derivatives; original scans and team labels unchanged')
if __name__=='__main__':prepare()
