"""Minimal OpenAI-compatible inference server.
Run after selecting and training the final model/adapter.
"""
import os,torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer,AutoModelForCausalLM
MODEL_ID=os.environ.get('MODEL_ID','Qwen/Qwen3-1.7B-Base')
tok=AutoTokenizer.from_pretrained(MODEL_ID)
model=AutoModelForCausalLM.from_pretrained(MODEL_ID,device_map='auto',torch_dtype='auto')
model.eval()
app=FastAPI(title='Munyarwanda AI LLM API',version='0.1.0')
class Message(BaseModel): role:str; content:str
class Request(BaseModel): model:str='munyarwanda-ai'; messages:list[Message]; max_tokens:int=256; temperature:float=.2
@app.get('/health')
def health(): return {'status':'ok','model':MODEL_ID}
@app.post('/v1/chat/completions')
def chat(req:Request):
 text='\n'.join(f"{m.role}: {m.content}" for m in req.messages)+'\nassistant:'
 x=tok(text,return_tensors='pt').to(model.device)
 with torch.no_grad(): y=model.generate(**x,max_new_tokens=min(req.max_tokens,1024),do_sample=req.temperature>0,temperature=max(req.temperature,.01),pad_token_id=tok.eos_token_id)
 ans=tok.decode(y[0][x['input_ids'].shape[-1]:],skip_special_tokens=True)
 return {'id':'munyarwanda-'+str(abs(hash(ans))),'object':'chat.completion','choices':[{'index':0,'message':{'role':'assistant','content':ans},'finish_reason':'stop'}]}
if __name__=='__main__':
 import uvicorn; uvicorn.run(app,host='0.0.0.0',port=int(os.environ.get('PORT','8000')))
