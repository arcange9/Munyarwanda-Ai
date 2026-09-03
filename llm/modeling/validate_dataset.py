import argparse,json,os

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--report',default='artifacts/dataset_validation.json'); a=ap.parse_args()
    seen=set(); rows=0; bad=0; missing=0; duplicates=0
    with open(a.input,encoding='utf-8') as f:
      for line in f:
        rows+=1
        try: x=json.loads(line)
        except: bad+=1; continue
        msgs=x.get('messages')
        if not isinstance(msgs,list) or len(msgs)<2: missing+=1; continue
        if not all(isinstance(m,dict) and m.get('role') in {'system','user','assistant'} and isinstance(m.get('content'),str) and m['content'].strip() for m in msgs): missing+=1; continue
        key=json.dumps(msgs,ensure_ascii=False,sort_keys=True)
        if key in seen: duplicates+=1
        seen.add(key)
    os.makedirs(os.path.dirname(a.report),exist_ok=True)
    report={'rows':rows,'parse_errors':bad,'invalid_schema':missing,'exact_duplicates':duplicates,'status':'pass' if bad==missing==duplicates==0 else 'review'}
    json.dump(report,open(a.report,'w',encoding='utf-8'),indent=2,ensure_ascii=False); print(report)
if __name__=='__main__': main()
