import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { Loader2, AlertCircle, ArrowLeft, ArrowRight } from 'lucide-react'
import { MarkdownRenderer } from '../components/MarkdownRenderer'
import { Breadcrumbs } from '../components/Breadcrumbs'
import {
  fetchMarkdown,
  rewriteMarkdownLinks,
  normalizeDocPath,
  flattenNav,
} from '../lib/content'
import navigationData from '../data/navigation.json'
import type { NavigationData } from '../lib/content'

export function DocPage() {
  const { '*': splat } = useParams()
  const docPath = splat ? `/doc/${splat}` : '/doc/README'
  const [content, setContent] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  const normalized = normalizeDocPath(docPath)
  const nav = navigationData as NavigationData
  const flat = flattenNav(nav.sections)
  const currentIndex = flat.findIndex(
    (item) => item.path === docPath || item.path === `/doc/${normalized}` || `${item.path}/README` === docPath,
  )
  const prev = currentIndex > 0 ? flat[currentIndex - 1] : null
  const next = currentIndex >= 0 && currentIndex < flat.length - 1 ? flat[currentIndex + 1] : null

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)

    const tryFetch = async () => {
      try {
        const raw = await fetchMarkdown(docPath)
        if (!cancelled) {
          setContent(rewriteMarkdownLinks(raw, docPath))
          setLoading(false)
        }
      } catch {
        if (!cancelled) {
          setError(`Could not load: ${normalized}`)
          setLoading(false)
        }
      }
    }

    tryFetch()
    return () => {
      cancelled = true
    }
  }, [normalized, docPath])

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center py-24 text-slate-500">
        <Loader2 className="mb-4 h-8 w-8 animate-spin text-brand-500" />
        <p className="text-sm">Loading content...</p>
      </div>
    )
  }

  if (error || !content) {
    return (
      <div className="flex flex-col items-center justify-center py-24 text-center">
        <AlertCircle className="mb-4 h-10 w-10 text-red-400" />
        <h2 className="mb-2 font-sans text-xl font-semibold text-slate-900">Page not found</h2>
        <p className="mb-6 text-slate-500">{error}</p>
        <Link
          to="/doc/weeks/week-01"
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-700"
        >
          Start with Week 01
        </Link>
      </div>
    )
  }

  return (
    <div>
      <Breadcrumbs path={docPath} />
      <MarkdownRenderer content={content} />

      {(prev || next) && (
        <nav className="mt-16 flex flex-col gap-3 border-t border-slate-200 pt-8 sm:flex-row sm:justify-between">
          {prev ? (
            <Link
              to={prev.path}
              className="group flex items-center gap-2 rounded-xl border border-slate-200 p-4 transition hover:border-brand-300 hover:bg-brand-50/50 sm:max-w-[48%]"
            >
              <ArrowLeft className="h-4 w-4 shrink-0 text-slate-400 group-hover:text-brand-600" />
              <div className="min-w-0">
                <p className="text-xs text-slate-500">Previous</p>
                <p className="truncate text-sm font-medium text-slate-800">{prev.title}</p>
              </div>
            </Link>
          ) : (
            <div />
          )}
          {next && (
            <Link
              to={next.path}
              className="group flex items-center justify-end gap-2 rounded-xl border border-slate-200 p-4 text-right transition hover:border-brand-300 hover:bg-brand-50/50 sm:max-w-[48%]"
            >
              <div className="min-w-0">
                <p className="text-xs text-slate-500">Next</p>
                <p className="truncate text-sm font-medium text-slate-800">{next.title}</p>
              </div>
              <ArrowRight className="h-4 w-4 shrink-0 text-slate-400 group-hover:text-brand-600" />
            </Link>
          )}
        </nav>
      )}
    </div>
  )
}
