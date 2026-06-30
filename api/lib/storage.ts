import { kv } from '@vercel/kv'

export const EVENTS_KEY = 'analytics:events'
export const MAX_EVENTS = 10_000

export interface AnalyticsEvent {
  id: string
  timestamp: string
  sessionId: string
  path: string
  referrer: string
  userAgent: string
  ip: string
  city: string
  country: string
  region: string
}

export function kvConfigured(): boolean {
  return Boolean(process.env.KV_REST_API_URL && process.env.KV_REST_API_TOKEN)
}

export async function appendEvent(event: AnalyticsEvent): Promise<void> {
  if (!kvConfigured()) {
    console.warn('[analytics] Vercel KV not configured — event dropped')
    return
  }
  await kv.lpush(EVENTS_KEY, JSON.stringify(event))
  await kv.ltrim(EVENTS_KEY, 0, MAX_EVENTS - 1)
}

export async function getEvents(limit = 5000): Promise<AnalyticsEvent[]> {
  if (!kvConfigured()) return []
  const raw = await kv.lrange<string>(EVENTS_KEY, 0, limit - 1)
  return raw
    .map((item) => {
      try {
        return typeof item === 'string' ? (JSON.parse(item) as AnalyticsEvent) : (item as AnalyticsEvent)
      } catch {
        return null
      }
    })
    .filter((e): e is AnalyticsEvent => e !== null)
}
