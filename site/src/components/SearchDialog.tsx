import { useEffect, useState, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import { Search, X, FileText } from 'lucide-react'
import type { NavItem } from '../lib/content'
import { flattenNav } from '../lib/content'
import navigationData from '../data/navigation.json'
import type { NavigationData } from '../lib/content'

interface SearchDialogProps {
  open: boolean
  onClose: () => void
}

export function SearchDialog({ open, onClose }: SearchDialogProps) {
  const [query, setQuery] = useState('')
  const navigate = useNavigate()
  const nav = navigationData as NavigationData
  const allItems = flattenNav(nav.sections)

  const filtered = query.trim()
    ? allItems.filter((item) => item.title.toLowerCase().includes(query.toLowerCase())).slice(0, 12)
    : allItems.filter((item) => item.path.includes('week-')).slice(0, 8)

  const select = useCallback(
    (item: NavItem) => {
      navigate(item.path)
      onClose()
      setQuery('')
    },
    [navigate, onClose],
  )

  useEffect(() => {
    if (!open) return
    const handler = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [open, onClose])

  if (!open) return null

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center bg-surface-950/50 px-4 pt-[15vh] backdrop-blur-sm">
      <button type="button" className="absolute inset-0" onClick={onClose} aria-label="Close search" />
      <div className="relative w-full max-w-xl overflow-hidden rounded-2xl bg-white shadow-2xl ring-1 ring-slate-200">
        <div className="flex items-center gap-3 border-b border-slate-100 px-4">
          <Search className="h-5 w-5 text-slate-400" />
          <input
            type="search"
            autoFocus
            placeholder="Search weeks, modules, interview prep..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="flex-1 border-0 bg-transparent py-4 text-base text-slate-900 placeholder:text-slate-400 focus:outline-none focus:ring-0"
          />
          <button type="button" onClick={onClose} className="rounded-lg p-1.5 text-slate-400 hover:bg-slate-100">
            <X className="h-4 w-4" />
          </button>
        </div>
        <ul className="max-h-80 overflow-y-auto py-2">
          {filtered.length === 0 ? (
            <li className="px-4 py-8 text-center text-sm text-slate-500">No results found</li>
          ) : (
            filtered.map((item) => (
              <li key={item.path}>
                <button
                  type="button"
                  onClick={() => select(item)}
                  className="flex w-full items-center gap-3 px-4 py-2.5 text-left hover:bg-slate-50"
                >
                  <FileText className="h-4 w-4 shrink-0 text-slate-400" />
                  <span className="truncate text-sm font-medium text-slate-800">{item.title}</span>
                </button>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  )
}
