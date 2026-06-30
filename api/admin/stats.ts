import type { VercelRequest, VercelResponse } from '@vercel/node'
import { checkAdminAuth } from '../lib/auth'
import { getEvents, kvConfigured } from '../lib/storage'

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  if (!checkAdminAuth(req)) {
    return res.status(401).json({ error: 'Unauthorized' })
  }

  const events = await getEvents()

  const pageViews: Record<string, number> = {}
  const sessions = new Map<
    string,
    { sessionId: string; ip: string; city: string; country: string; region: string; firstSeen: string; lastSeen: string; pages: Set<string>; hits: number }
  >()

  for (const e of events) {
    pageViews[e.path] = (pageViews[e.path] || 0) + 1

    const existing = sessions.get(e.sessionId)
    if (existing) {
      existing.hits++
      existing.pages.add(e.path)
      if (e.timestamp > existing.lastSeen) existing.lastSeen = e.timestamp
      if (e.timestamp < existing.firstSeen) existing.firstSeen = e.timestamp
    } else {
      sessions.set(e.sessionId, {
        sessionId: e.sessionId,
        ip: e.ip,
        city: e.city,
        country: e.country,
        region: e.region,
        firstSeen: e.timestamp,
        lastSeen: e.timestamp,
        pages: new Set([e.path]),
        hits: 1,
      })
    }
  }

  const topPages = Object.entries(pageViews)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 30)
    .map(([path, views]) => ({ path, views }))

  const cityBreakdown: Record<string, number> = {}
  const countryBreakdown: Record<string, number> = {}
  for (const s of sessions.values()) {
    const cityKey = `${s.city}, ${s.country}`
    cityBreakdown[cityKey] = (cityBreakdown[cityKey] || 0) + 1
    countryBreakdown[s.country] = (countryBreakdown[s.country] || 0) + 1
  }

  const visitors = [...sessions.values()]
    .sort((a, b) => b.lastSeen.localeCompare(a.lastSeen))
    .slice(0, 100)
    .map((s) => ({
      sessionId: s.sessionId.slice(0, 8) + '…',
      ip: s.ip,
      city: s.city,
      country: s.country,
      region: s.region,
      firstSeen: s.firstSeen,
      lastSeen: s.lastSeen,
      pageCount: s.pages.size,
      hits: s.hits,
      pages: [...s.pages].slice(0, 10),
    }))

  const recent = events.slice(0, 50).map((e) => ({
    timestamp: e.timestamp,
    path: e.path,
    ip: e.ip,
    city: e.city,
    country: e.country,
    sessionId: e.sessionId.slice(0, 8) + '…',
  }))

  return res.status(200).json({
    kvReady: kvConfigured(),
    summary: {
      totalPageViews: events.length,
      uniqueVisitors: sessions.size,
      topPagesCount: topPages.length,
    },
    topPages,
    cityBreakdown: Object.entries(cityBreakdown)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 20)
      .map(([city, count]) => ({ city, count })),
    countryBreakdown: Object.entries(countryBreakdown)
      .sort((a, b) => b[1] - a[1])
      .map(([country, count]) => ({ country, count })),
    visitors,
    recent,
  })
}
