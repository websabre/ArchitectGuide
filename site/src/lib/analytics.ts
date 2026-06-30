const SESSION_KEY = 'ag_session_id'
const ADMIN_TOKEN_KEY = 'ag_admin_token'

export function getSessionId(): string {
  let id = localStorage.getItem(SESSION_KEY)
  if (!id) {
    id = crypto.randomUUID()
    localStorage.setItem(SESSION_KEY, id)
  }
  return id
}

export function getAdminToken(): string | null {
  return sessionStorage.getItem(ADMIN_TOKEN_KEY)
}

export function setAdminToken(token: string): void {
  sessionStorage.setItem(ADMIN_TOKEN_KEY, token)
}

export function clearAdminToken(): void {
  sessionStorage.removeItem(ADMIN_TOKEN_KEY)
}

export async function trackPageView(path: string): Promise<void> {
  try {
    await fetch('/api/track', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sessionId: getSessionId(),
        path,
        referrer: document.referrer,
        userAgent: navigator.userAgent,
      }),
      keepalive: true,
    })
  } catch {
    // silent — analytics should not break the app
  }
}

export interface AdminStats {
  kvReady: boolean
  summary: {
    totalPageViews: number
    uniqueVisitors: number
    topPagesCount: number
  }
  topPages: { path: string; views: number }[]
  cityBreakdown: { city: string; count: number }[]
  countryBreakdown: { country: string; count: number }[]
  visitors: {
    sessionId: string
    ip: string
    city: string
    country: string
    region: string
    firstSeen: string
    lastSeen: string
    pageCount: number
    hits: number
    pages: string[]
  }[]
  recent: {
    timestamp: string
    path: string
    ip: string
    city: string
    country: string
    sessionId: string
  }[]
}

export async function adminLogin(password: string): Promise<{ token: string; kvReady: boolean }> {
  const res = await fetch('/api/admin/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password }),
  })
  if (!res.ok) {
    const data = await res.json().catch(() => ({}))
    throw new Error((data as { error?: string }).error || 'Login failed')
  }
  return res.json()
}

export async function fetchAdminStats(): Promise<AdminStats> {
  const token = getAdminToken()
  if (!token) throw new Error('Not authenticated')

  const res = await fetch('/api/admin/stats', {
    headers: { Authorization: `Bearer ${token}` },
  })
  if (res.status === 401) {
    clearAdminToken()
    throw new Error('Session expired')
  }
  if (!res.ok) throw new Error('Failed to load stats')
  return res.json()
}
