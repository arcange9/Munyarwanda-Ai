"""Download only sources explicitly approved in manifests/source_manifest.json.
For gated Hugging Face datasets, authenticate first and accept their terms.
"""
import argparse,json,os
from datasets import load_dataset

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',default='manifests/source_manifest.json'); ap.add_argument('--out',default='data/raw'); ap.add_argument('--id'); args=ap.parse_args()
    manifest=json.load(open(args.source,encoding='utf-8'))
    for s in manifest:
        if not s.get('approved_for_pipeline'): continue
        if args.id and s['id']!=args.id: continue
        print('Acquiring',s['id'],s['repo'])
        ds=load_dataset(s['repo'])
        path=os.path.join(args.out,s['id']); os.makedirs(path,exist_ok=True)
        for split,table in ds.items(): table.to_json(os.path.join(path,f'{split}.jsonl'),force_ascii=False)
        with open(os.path.join(path,'PROVENANCE.json'),'w',encoding='utf-8') as f: json.dump(s,f,indent=2,ensure_ascii=False)
if __name__=='__main__': main()
