'use client'

import { FormEvent, useState } from 'react'

export default function ChatPage(){
  const [message,setMessage]=useState('')
  const [answer,setAnswer]=useState('')
  const [sources,setSources]=useState<any[]>([])
  const [webSearch,setWebSearch]=useState(false)
  const [loading,setLoading]=useState(false)

  async function send(e:FormEvent){
    e.preventDefault()
    if(!message.trim() || loading) return
    setLoading(true); setAnswer(''); setSources([])
    try{
      const res=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message,webSearch})})
      if(!res.ok) throw new Error('Request failed')
      const reader=res.body?.getReader(); const decoder=new TextDecoder()
      if(!reader) throw new Error('Streaming unavailable')
      let buffer=''
      while(true){
        const {done,value}=await reader.read(); if(done) break
        buffer+=decoder.decode(value,{stream:true})
        const events=buffer.split('\n\n'); buffer=events.pop()||''
        for(const event of events){
          const line=event.split('\n').find(x=>x.startsWith('data: ')); if(!line) continue
          const payload=line.slice(6); if(payload==='[DONE]') continue
          const data=JSON.parse(payload)
          if(data.text) setAnswer(prev=>prev+data.text)
          if(data.sources) setSources(data.sources)
          if(data.error) setAnswer(data.error)
        }
      }
    }catch(err){ setAnswer('Ntibyashobotse kurangiza iki kibazo. Ongera ugerageze.') }
    finally{ setLoading(false) }
  }

  return <main className="min-h-screen bg-black text-white px-5 py-10">
    <div className="mx-auto max-w-4xl">
      <header className="mb-8"><p className="text-sm uppercase tracking-[0.3em] text-white/50">MUNYARWANDA AI</p><h1 className="mt-2 text-4xl font-semibold">Kinyarwanda-first AI assistant</h1></header>
      <form onSubmit={send} className="space-y-4">
        <textarea value={message} onChange={e=>setMessage(e.target.value)} placeholder="Andika ikibazo cyawe mu Kinyarwanda..." className="min-h-36 w-full rounded-2xl border border-white/15 bg-white/5 p-5 outline-none" />
        <div className="flex flex-wrap items-center gap-3">
          <button type="button" onClick={()=>setWebSearch(v=>!v)} className="rounded-full border border-white/20 px-4 py-2 text-sm">{webSearch?'Web research: ON':'Search web'}</button>
          <button disabled={loading} className="rounded-full bg-white px-5 py-2 font-medium text-black disabled:opacity-50">{loading?'Biratekerezwa...':'Ohereza'}</button>
        </div>
      </form>
      <section className="mt-10 whitespace-pre-wrap rounded-2xl border border-white/10 bg-white/[0.03] p-6 leading-7">{answer||'Igisubizo kizagaragara hano.'}</section>
      {sources.length>0 && <section className="mt-6"><h2 className="mb-3 text-lg font-medium">Sources</h2><div className="space-y-2">{sources.map((s,i)=><a key={i} href={s.url} target="_blank" rel="noreferrer" className="block rounded-xl border border-white/10 p-4 hover:bg-white/5"><div className="font-medium">{s.title||s.url}</div><div className="mt-1 text-sm text-white/50">{s.url}</div></a>)}</div></section>}
    </div>
  </main>
}
