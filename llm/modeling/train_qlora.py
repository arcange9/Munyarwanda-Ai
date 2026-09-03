import argparse,yaml,os,torch

def smoke():
 from transformers import AutoTokenizer,AutoModelForCausalLM
 from peft import LoraConfig,get_peft_model
 mid='hf-internal-testing/tiny-random-LlamaForCausalLM'; tok=AutoTokenizer.from_pretrained(mid); model=AutoModelForCausalLM.from_pretrained(mid)
 tok.pad_token=tok.pad_token or tok.eos_token
 peft=get_peft_model(model,LoraConfig(r=4,lora_alpha=8,lora_dropout=.05,target_modules=['q_proj','v_proj'],task_type='CAUSAL_LM'))
 b=tok(['Muraho neza.','Sobanura Python mu Kinyarwanda.']*2,padding=True,return_tensors='pt'); loss=peft(**b,labels=b['input_ids']).loss; loss.backward(); os.makedirs('artifacts/smoke',exist_ok=True); peft.save_pretrained('artifacts/smoke'); print({'status':'pass','loss':float(loss.detach())})

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--config',default='configs/phase32.yaml'); ap.add_argument('--smoke-test',action='store_true'); ap.add_argument('--run-training',action='store_true'); a=ap.parse_args()
 if a.smoke_test: smoke(); return
 cfg=yaml.safe_load(open(a.config,encoding='utf-8'))
 if cfg['base_model']=='CHANGE_AFTER_BENCHMARK': raise SystemExit('Select the measured winner in configs/phase32.yaml first.')
 if not a.run_training: raise SystemExit('Pass --run-training to start real training.')
 from datasets import load_dataset
 from transformers import AutoTokenizer,AutoModelForCausalLM,TrainingArguments
 from peft import LoraConfig
 from trl import SFTTrainer
 train=load_dataset('json',data_files=cfg['dataset_path'],split='train'); val=load_dataset('json',data_files=cfg['validation_path'],split='train')
 tok=AutoTokenizer.from_pretrained(cfg['base_model']); tok.pad_token=tok.pad_token or tok.eos_token
 model=AutoModelForCausalLM.from_pretrained(cfg['base_model'],device_map='auto',torch_dtype='auto')
 peft=LoraConfig(r=cfg['lora_r'],lora_alpha=cfg['lora_alpha'],lora_dropout=cfg['lora_dropout'],target_modules=['q_proj','k_proj','v_proj','o_proj'],task_type='CAUSAL_LM')
 args=TrainingArguments(output_dir=cfg['output_dir'],num_train_epochs=cfg['num_train_epochs'],per_device_train_batch_size=cfg['per_device_train_batch_size'],gradient_accumulation_steps=cfg['gradient_accumulation_steps'],learning_rate=cfg['learning_rate'],warmup_ratio=cfg['warmup_ratio'],logging_steps=cfg['logging_steps'],save_steps=cfg['save_steps'],bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),fp16=torch.cuda.is_available() and not torch.cuda.is_bf16_supported(),report_to='none')
 trainer=SFTTrainer(model=model,args=args,train_dataset=train,eval_dataset=val,peft_config=peft,processing_class=tok)
 trainer.train(); trainer.save_model(cfg['output_dir'])
if __name__=='__main__': main()
