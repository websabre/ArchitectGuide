import type { VercelRequest, VercelResponse } from '@vercel/node'
import { appendEvent, type AnalyticsEvent } from './lib/storage'

function clientIp(req: VercelRequest): string {
  const forwarded = req.headers['x-forwarded-for']
  if (typeof forwarded === 'string') return forwarded.split(',')[0].trim()
  if (Array.isArray(forwarded)) return forwarded[0]
  return (req.headers['x-real-ip'] as string) || 'unknown'
}

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Origin', '*')
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS')
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type')
    return res.status(204).end()
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  const body = req.body as { sessionId?: string; path?: string; referrer?: string; userAgent?: string }
  if (!body?.sessionId || !body?.path) {
    return res.status(400).json({ error: 'sessionId and path required' })
  }

  // Skip admin routes from analytics noise
  if (body.path.startsWith('/admin')) {
    return res.status(200).json({ ok: true, skipped: true })
  }

  const event: AnalyticsEvent = {
    id: `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`,
    timestamp: new Date().toISOString(),
    sessionId: body.sessionId,
    path: body.path,
    referrer: body.referrer || '',
    userAgent: body.userAgent || '',
    ip: clientIp(req),
    city: (req.headers['x-vercel-ip-city'] as string) || 'Unknown',
    country: (req.headers['x-vercel-ip-country'] as string) || 'Unknown',
    region: (req.headers['x-vercel-ip-country-region'] as string) || '',
  }

  try {
    await appendEvent(event)
    return res.status(200).json({ ok: true })
  } catch (err) {
    console.error('[analytics] track error', err)
    return res.status(500).json({ error: 'Failed to record event' })
  }
}
