import { NextRequest } from 'next/server'
import { z } from 'zod'
import { googleSearch } from '@/lib/web-search'

const ResearchSchema = z.object({
  query: z.string().min(2).max(1000),
  limit: z.number().int().min(1).max(10).optional(),
})

export const runtime = 'nodejs'

export async function POST(req: NextRequest) {
  try {
    const parsed = ResearchSchema.safeParse(await req.json())
    if (!parsed.success) return Response.json({ error: 'Invalid research request' }, { status: 400 })
    const results = await googleSearch(parsed.data.query, parsed.data.limit ?? 6, req.signal)
    return Response.json({ query: parsed.data.query, results })
  } catch (error) {
    console.error('[research]', error)
    return Response.json({ error: 'Web research is currently unavailable.' }, { status: 503 })
  }
}
