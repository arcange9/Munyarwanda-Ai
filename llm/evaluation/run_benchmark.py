import argparse,json,time,os,torch
from transformers import AutoTokenizer,AutoModelForCausalLM

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--model',required=True); ap.add_argument('--benchmark',default='data/benchmark/benchmark_v1.jsonl'); ap.add_argument('--max-new-tokens',type=int,default=160); a=ap.parse_args()
 tok=AutoTokenizer.from_pretrained(a.model); model=AutoModelForCausalLM.from_pretrained(a.model,device_map='auto',torch_dtype='auto'); model.eval(); rows=[]
 for line in open(a.benchmark,encoding='utf-8'):
  item=json.loads(line); prompt=item['prompt']; inputs=tok(prompt,return_tensors='pt').to(model.device); t=time.perf_counter()
  with torch.no_grad(): out=model.generate(**inputs,max_new_tokens=a.max_new_tokens,do_sample=False,pad_token_id=tok.eos_token_id)
  latency=time.perf_counter()-t; text=tok.decode(out[0][inputs['input_ids'].shape[-1]:],skip_special_tokens=True); rows.append({**item,'response':text,'latency_s':latency})
 os.makedirs('artifacts',exist_ok=True); path='artifacts/benchmark_'+a.model.replace('/','_')+'.json'; json.dump({'model':a.model,'results':rows},open(path,'w',encoding='utf-8'),indent=2,ensure_ascii=False); print(path)
if __name__=='__main__': main()
