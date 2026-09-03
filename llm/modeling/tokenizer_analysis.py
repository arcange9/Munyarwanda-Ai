import argparse,json,os,re
from transformers import AutoTokenizer

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--model',required=True); ap.add_argument('--text',required=True); ap.add_argument('--limit',type=int,default=5000); a=ap.parse_args()
 tok=AutoTokenizer.from_pretrained(a.model); words=tokens=sentences=0; samples=0
 with open(a.text,encoding='utf-8') as f:
  for i,line in enumerate(f):
   if i>=a.limit: break
   try: x=json.loads(line); text=x.get('text','')
   except: continue
   samples+=1; words+=len(text.split()); tokens+=len(tok.encode(text,add_special_tokens=False)); sentences+=len(re.findall(r'[.!?]+',text)) or 1
 out={'model':a.model,'samples':samples,'words':words,'tokens':tokens,'tokens_per_word':tokens/max(words,1),'tokens_per_sentence':tokens/max(sentences,1)}
 os.makedirs('artifacts',exist_ok=True); json.dump(out,open('artifacts/tokenizer_'+a.model.split('/')[-1]+'.json','w'),indent=2); print(out)
if __name__=='__main__': main()
