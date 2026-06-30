import { useState, useEffect, useCallback } from 'react'
import { Link } from 'react-router-dom'
import {
  BarChart3,
  Users,
  Eye,
  Globe,
  LogOut,
  RefreshCw,
  Lock,
  AlertTriangle,
} from 'lucide-react'
import {
  adminLogin,
  fetchAdminStats,
  getAdminToken,
  setAdminToken,
  clearAdminToken,
  type AdminStats,
} from '../lib/analytics'

function StatCard({ label, value, icon: Icon }: { label: string; value: number | string; icon: typeof Eye }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex items-center justify-between">
        <p className="text-sm font-medium text-slate-500">{label}</p>
        <Icon className="h-5 w-5 text-brand-500" />
      </div>
      <p className="mt-2 font-sans text-3xl font-bold text-slate-900">{value}</p>
    </div>
  )
}

function LoginForm({ onSuccess }: { onSuccess: () => void }) {
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      const { token } = await adminLogin(password)
      setAdminToken(token)
      onSuccess()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-surface-900 px-4">
      <form onSubmit={submit} className="w-full max-w-sm rounded-2xl border border-surface-800 bg-surface-900 p-8 shadow-xl">
        <div className="mb-6 flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-brand-600">
            <Lock className="h-5 w-5 text-white" />
          </div>
          <div>
            <h1 className="font-sans text-lg font-bold text-white">Admin</h1>
            <p className="text-xs text-slate-500">Architect Guide Analytics</p>
          </div>
        </div>
        <label className="mb-1 block text-xs font-medium text-slate-400">Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mb-4 w-full rounded-lg border border-surface-800 bg-surface-800 px-3 py-2.5 text-white focus:border-brand-500 focus:outline-none"
          placeholder="ADMIN_PASSWORD"
          autoComplete="current-password"
        />
        {error && <p className="mb-3 text-sm text-red-400">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-lg bg-brand-600 py-2.5 text-sm font-semibold text-white hover:bg-brand-500 disabled:opacity-50"
        >
          {loading ? 'Signing in…' : 'Sign in'}
        </button>
        <Link to="/" className="mt-4 block text-center text-xs text-slate-500 hover:text-brand-400">
          ← Back to site
        </Link>
      </form>
    </div>
  )
}

function Dashboard({ stats, onRefresh, onLogout }: { stats: AdminStats; onRefresh: () => void; onLogout: () => void }) {
  return (
    <div className="min-h-screen bg-slate-50">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 lg:px-8">
          <div className="flex items-center gap-3">
            <BarChart3 className="h-6 w-6 text-brand-600" />
            <div>
              <h1 className="font-sans text-lg font-bold text-slate-900">Analytics Dashboard</h1>
              <p className="text-xs text-slate-500">Architect Guide · admin</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onRefresh}
              className="flex items-center gap-1.5 rounded-lg border border-slate-200 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-50"
            >
              <RefreshCw className="h-4 w-4" />
              Refresh
            </button>
            <button
              type="button"
              onClick={onLogout}
              className="flex items-center gap-1.5 rounded-lg border border-slate-200 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-50"
            >
              <LogOut className="h-4 w-4" />
              Logout
            </button>
            <Link to="/" className="rounded-lg bg-brand-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-brand-500">
              View site
            </Link>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-4 py-8 lg:px-8">
        {!stats.kvReady && (
          <div className="mb-6 flex items-start gap-3 rounded-xl border border-amber-200 bg-amber-50 p-4 text-sm text-amber-900">
            <AlertTriangle className="mt-0.5 h-5 w-5 shrink-0" />
            <div>
              <p className="font-semibold">Vercel KV not connected</p>
              <p className="mt-1 text-amber-800">
                Add a KV store in Vercel → Storage → Connect to project. Events will appear after KV is linked and
                ADMIN_PASSWORD is set.
              </p>
            </div>
          </div>
        )}

        <div className="mb-8 grid gap-4 sm:grid-cols-3">
          <StatCard label="Total page views" value={stats.summary.totalPageViews} icon={Eye} />
          <StatCard label="Unique visitors" value={stats.summary.uniqueVisitors} icon={Users} />
          <StatCard label="Tracked pages" value={stats.summary.topPagesCount} icon={Globe} />
        </div>

        <div className="mb-8 grid gap-6 lg:grid-cols-2">
          <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <h2 className="mb-4 font-sans text-sm font-semibold text-slate-900">Top pages</h2>
            <div className="max-h-80 overflow-y-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b text-left text-xs text-slate-500">
                    <th className="pb-2 pr-2">Path</th>
                    <th className="pb-2 text-right">Views</th>
                  </tr>
                </thead>
                <tbody>
                  {stats.topPages.map((row) => (
                    <tr key={row.path} className="border-b border-slate-50">
                      <td className="py-2 pr-2 font-mono text-xs text-slate-700">{row.path}</td>
                      <td className="py-2 text-right font-medium">{row.views}</td>
                    </tr>
                  ))}
                  {stats.topPages.length === 0 && (
                    <tr>
                      <td colSpan={2} className="py-8 text-center text-slate-400">
                        No data yet
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>

          <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <h2 className="mb-4 font-sans text-sm font-semibold text-slate-900">Visitors by city</h2>
            <div className="max-h-80 overflow-y-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b text-left text-xs text-slate-500">
                    <th className="pb-2">City</th>
                    <th className="pb-2 text-right">Visitors</th>
                  </tr>
                </thead>
                <tbody>
                  {stats.cityBreakdown.map((row) => (
                    <tr key={row.city} className="border-b border-slate-50">
                      <td className="py-2">{row.city}</td>
                      <td className="py-2 text-right font-medium">{row.count}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </div>

        <section className="mb-8 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
          <h2 className="mb-4 font-sans text-sm font-semibold text-slate-900">Recent visitors</h2>
          <div className="overflow-x-auto">
            <table className="w-full min-w-[800px] text-sm">
              <thead>
                <tr className="border-b text-left text-xs text-slate-500">
                  <th className="pb-2 pr-3">Session</th>
                  <th className="pb-2 pr-3">IP</th>
                  <th className="pb-2 pr-3">Location</th>
                  <th className="pb-2 pr-3">Pages</th>
                  <th className="pb-2 pr-3">Hits</th>
                  <th className="pb-2">Last seen</th>
                </tr>
              </thead>
              <tbody>
                {stats.visitors.map((v) => (
                  <tr key={v.sessionId + v.ip} className="border-b border-slate-50 align-top">
                    <td className="py-2 pr-3 font-mono text-xs">{v.sessionId}</td>
                    <td className="py-2 pr-3 font-mono text-xs">{v.ip}</td>
                    <td className="py-2 pr-3">
                      {v.city}, {v.country}
                      {v.region && <span className="text-slate-400"> ({v.region})</span>}
                    </td>
                    <td className="py-2 pr-3">
                      <span className="font-medium">{v.pageCount}</span>
                      <ul className="mt-1 max-w-xs text-xs text-slate-500">
                        {v.pages.map((p) => (
                          <li key={p} className="truncate font-mono">
                            {p}
                          </li>
                        ))}
                      </ul>
                    </td>
                    <td className="py-2 pr-3">{v.hits}</td>
                    <td className="py-2 whitespace-nowrap text-xs text-slate-500">
                      {new Date(v.lastSeen).toLocaleString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
          <h2 className="mb-4 font-sans text-sm font-semibold text-slate-900">Live feed (latest 50 events)</h2>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b text-left text-xs text-slate-500">
                  <th className="pb-2 pr-3">Time</th>
                  <th className="pb-2 pr-3">Path</th>
                  <th className="pb-2 pr-3">IP</th>
                  <th className="pb-2 pr-3">City</th>
                  <th className="pb-2">Session</th>
                </tr>
              </thead>
              <tbody>
                {stats.recent.map((e, i) => (
                  <tr key={i} className="border-b border-slate-50">
                    <td className="py-1.5 pr-3 text-xs text-slate-500">{new Date(e.timestamp).toLocaleString()}</td>
                    <td className="py-1.5 pr-3 font-mono text-xs">{e.path}</td>
                    <td className="py-1.5 pr-3 font-mono text-xs">{e.ip}</td>
                    <td className="py-1.5 pr-3 text-xs">{e.city}</td>
                    <td className="py-1.5 font-mono text-xs">{e.sessionId}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <p className="mt-8 text-center text-xs text-slate-400">
          IP and location from Vercel edge headers. Ensure privacy compliance for your jurisdiction (GDPR, etc.).
        </p>
      </main>
    </div>
  )
}

export function AdminPage() {
  const [authed, setAuthed] = useState(!!getAdminToken())
  const [stats, setStats] = useState<AdminStats | null>(null)
  const [error, setError] = useState('')

  const load = useCallback(async () => {
    try {
      const data = await fetchAdminStats()
      setStats(data)
      setError('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load')
      if (err instanceof Error && err.message === 'Session expired') setAuthed(false)
    }
  }, [])

  useEffect(() => {
    if (authed) load()
  }, [authed, load])

  const logout = () => {
    clearAdminToken()
    setAuthed(false)
    setStats(null)
  }

  if (!authed) return <LoginForm onSuccess={() => setAuthed(true)} />

  if (!stats && !error) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-slate-50">
        <RefreshCw className="h-8 w-8 animate-spin text-brand-500" />
      </div>
    )
  }

  if (error && !stats) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4 bg-slate-50">
        <p className="text-red-600">{error}</p>
        <button type="button" onClick={() => setAuthed(false)} className="text-sm text-brand-600">
          Back to login
        </button>
      </div>
    )
  }

  return stats ? <Dashboard stats={stats} onRefresh={load} onLogout={logout} /> : null
}
