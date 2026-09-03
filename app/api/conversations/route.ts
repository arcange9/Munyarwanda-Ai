import { NextRequest, NextResponse } from 'next/server'
import { getServerSession } from 'next-auth'
import { authOptions } from '@/lib/auth'
import { prisma } from '@/lib/prisma'
import { z } from 'zod'
async function requireUser(){const session=await getServerSession(authOptions);return (session as any)?.uid?String((session as any).uid):null}
export async function GET(){const userId=await requireUser();if(!userId)return NextResponse.json({error:'Unauthorized'},{status:401});const convos=await prisma.conversation.findMany({where:{userId},orderBy:{updatedAt:'desc'},include:{messages:{orderBy:{createdAt:'asc'}}}});return NextResponse.json(convos)}
export async function POST(req:NextRequest){const userId=await requireUser();if(!userId)return NextResponse.json({error:'Unauthorized'},{status:401});const parsed=z.object({title:z.string().trim().max(100).optional()}).safeParse(await req.json().catch(()=>({})));if(!parsed.success)return NextResponse.json({error:'Invalid request'},{status:400});const convo=await prisma.conversation.create({data:{userId,title:parsed.data.title||'New conversation'}});return NextResponse.json(convo,{status:201})}
