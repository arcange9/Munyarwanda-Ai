import { NextRequest, NextResponse } from 'next/server'
import { getServerSession } from 'next-auth'
import { authOptions } from '@/lib/auth'
import { prisma } from '@/lib/prisma'
import { z } from 'zod'
async function requireUser(){const session=await getServerSession(authOptions);return (session as any)?.uid?String((session as any).uid):null}
export async function GET(_:NextRequest,{params}:{params:{id:string}}){const userId=await requireUser();if(!userId)return NextResponse.json({error:'Unauthorized'},{status:401});const convo=await prisma.conversation.findFirst({where:{id:params.id,userId},include:{messages:{orderBy:{createdAt:'asc'}}}});if(!convo)return NextResponse.json({error:'Not found'},{status:404});return NextResponse.json(convo)}
export async function DELETE(_:NextRequest,{params}:{params:{id:string}}){const userId=await requireUser();if(!userId)return NextResponse.json({error:'Unauthorized'},{status:401});const result=await prisma.conversation.deleteMany({where:{id:params.id,userId}});if(!result.count)return NextResponse.json({error:'Not found'},{status:404});return NextResponse.json({ok:true})}
export async function PATCH(req:NextRequest,{params}:{params:{id:string}}){const userId=await requireUser();if(!userId)return NextResponse.json({error:'Unauthorized'},{status:401});const parsed=z.object({title:z.string().trim().min(1).max(100)}).safeParse(await req.json());if(!parsed.success)return NextResponse.json({error:'Invalid request'},{status:400});const result=await prisma.conversation.updateMany({where:{id:params.id,userId},data:{title:parsed.data.title}});if(!result.count)return NextResponse.json({error:'Not found'},{status:404});return NextResponse.json({ok:true})}
