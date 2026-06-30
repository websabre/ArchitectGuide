import { useState, useMemo, useEffect } from 'react'
import { Link, useLocation } from 'react-router-dom'
import {
  BookOpen,
  Calendar,
  Library,
  GraduationCap,
  Home,
  ChevronDown,
  ChevronRight,
  Search,
} from 'lucide-react'
import type { NavItem, NavSection } from '../lib/content'
import {
  categorizeNavigation,
  isPathActive,
  detectActiveTab,
  type NavTab,
} from '../lib/nav-helpers'

interface SidebarProps {
  sections: NavSection[]
  mobileOpen: boolean
  onClose: () => void
  onSearchClick: () => void
}

const TABS: { id: NavTab; label: string; icon: typeof Home }[] = [
  { id: 'start', label: 'Start', icon: Home },
  { id: 'weeks', label: 'Weeks', icon: Calendar },
  { id: 'library', label: 'Library', icon: Library },
  { id: 'program', label: 'Program', icon: GraduationCap },
]

function SimpleLink({ item, onNavigate }: { item: NavItem; onNavigate: () => void }) {
  const location = useLocation()
  const active = isPathActive(location.pathname, item.path)
  return (
    <Link
      to={item.path}
      onClick={onNavigate}
      className={`block rounded-lg px-3 py-2 text-sm transition ${active ? 'nav-link-active' : 'nav-link'}`}
    >
      {item.title}
    </Link>
  )
}

function MonthBlock({
  month,
  defaultOpen,
  onNavigate,
}: {
  month: NavSection
  defaultOpen: boolean
  onNavigate: () => void
}) {
  const [open, setOpen] = useState(defaultOpen)
  const location = useLocation()
  const monthActive = month.items.some(
    (w) => location.pathname === w.path || location.pathname.startsWith(w.path + '/'),
  )

  return (
    <div className="mb-1">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        className={`flex w-full items-center gap-2 rounded-lg px-2 py-2 text-left text-xs font-semibold uppercase tracking-wide transition hover:bg-surface-800 ${
          monthActive ? 'text-brand-300' : 'text-slate-500'
        }`}
      >
        {open ? <ChevronDown className="h-3.5 w-3.5 shrink-0" /> : <ChevronRight className="h-3.5 w-3.5 shrink-0" />}
        <span className="truncate">{month.title.replace(' — ', ' · ')}</span>
      </button>
      {open && (
        <div className="ml-1 mt-0.5 space-y-0.5 border-l border-surface-800 pl-2">
          {month.items.map((week) => {
            const active = isPathActive(location.pathname, week.path) || location.pathname.includes(week.path + '/')
            const short = week.title.replace(/^Week (\d+) — /, 'W$1 · ')
            return (
              <Link
                key={week.path}
                to={week.path}
                onClick={onNavigate}
                className={`block rounded-md px-2 py-1.5 text-sm transition ${
                  active ? 'bg-brand-600/20 font-medium text-brand-300' : 'text-slate-400 hover:bg-surface-800 hover:text-white'
                }`}
              >
                {short}
              </Link>
            )
          })}
        </div>
      )}
    </div>
  )
}

function LibrarySection({ section, onNavigate }: { section: NavSection; onNavigate: () => void }) {
  const location = useLocation()
  const hasActive = section.items.some(
    (i) =>
      isPathActive(location.pathname, i.path) ||
      i.children?.some((c) => isPathActive(location.pathname, c.path)),
  )
  const [expanded, setExpanded] = useState(hasActive)

  return (
    <div className="mb-3">
      <button
        type="button"
        onClick={() => setExpanded(!expanded)}
        className={`flex w-full items-center gap-2 px-2 py-1.5 text-left text-xs font-semibold uppercase tracking-wide ${
          hasActive ? 'text-brand-300' : 'text-slate-500'
        }`}
      >
        {expanded ? <ChevronDown className="h-3.5 w-3.5" /> : <ChevronRight className="h-3.5 w-3.5" />}
        {section.title}
      </button>
      {expanded && (
        <div className="mt-1 space-y-0.5 pl-1">
          {section.items.map((item) =>
            item.children && item.children.length > 0 ? (
              <LibraryFolder key={item.path} item={item} onNavigate={onNavigate} />
            ) : (
              <SimpleLink key={item.path} item={item} onNavigate={onNavigate} />
            ),
          )}
        </div>
      )}
    </div>
  )
}

function LibraryFolder({ item, onNavigate }: { item: NavItem; onNavigate: () => void }) {
  const location = useLocation()
  const [open, setOpen] = useState(
    isPathActive(location.pathname, item.path) ||
      item.children?.some((c) => isPathActive(location.pathname, c.path)),
  )

  return (
    <div>
      <div className="flex items-center gap-0.5">
        <button
          type="button"
          onClick={() => setOpen(!open)}
          className="shrink-0 rounded p-1 text-slate-500 hover:text-slate-300"
        >
          {open ? <ChevronDown className="h-3 w-3" /> : <ChevronRight className="h-3 w-3" />}
        </button>
        <Link
          to={item.path}
          onClick={onNavigate}
          className={`nav-link min-w-0 flex-1 truncate text-sm ${isPathActive(location.pathname, item.path) ? 'nav-link-active' : ''}`}
        >
          {item.title}
        </Link>
      </div>
      {open && item.children && (
        <div className="ml-4 space-y-0.5 border-l border-surface-800 pl-2">
          {item.children.slice(0, 12).map((child) => (
            <SimpleLink key={child.path} item={child} onNavigate={onNavigate} />
          ))}
          {item.children.length > 12 && (
            <p className="px-3 py-1 text-[10px] text-slate-600">+{item.children.length - 12} more — use ⌘K search</p>
          )}
        </div>
      )}
    </div>
  )
}

export function Sidebar({ sections, mobileOpen, onClose, onSearchClick }: SidebarProps) {
  const location = useLocation()
  const categorized = useMemo(() => categorizeNavigation(sections), [sections])
  const [activeTab, setActiveTab] = useState<NavTab>(() => detectActiveTab(location.pathname))
  const [weekFilter, setWeekFilter] = useState('')

  useEffect(() => {
    setActiveTab(detectActiveTab(location.pathname))
  }, [location.pathname])

  const filteredMonths = useMemo(() => {
    if (!weekFilter.trim()) return categorized.months
    const q = weekFilter.toLowerCase()
    return categorized.months
      .map((m) => ({
        ...m,
        items: m.items.filter(
          (w) => w.title.toLowerCase().includes(q) || w.path.includes(q.replace(/\D/g, '').padStart(2, '0')),
        ),
      }))
      .filter((m) => m.items.length > 0)
  }, [categorized.months, weekFilter])

  const activeMonthIndex = categorized.months.findIndex((m) =>
    m.items.some((w) => location.pathname.includes(w.path.split('/').pop() || '')),
  )

  return (
    <>
      {mobileOpen && (
        <button
          type="button"
          className="fixed inset-0 z-40 bg-surface-950/60 backdrop-blur-sm lg:hidden"
          onClick={onClose}
          aria-label="Close navigation"
        />
      )}

      <aside
        className={`fixed inset-y-0 left-0 z-50 flex w-72 flex-col border-r border-surface-800 bg-surface-900 transition-transform duration-300 lg:static lg:translate-x-0 ${
          mobileOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <div className="flex h-16 shrink-0 items-center gap-3 border-b border-surface-800 px-4">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-brand-600">
            <BookOpen className="h-5 w-5 text-white" />
          </div>
          <div className="min-w-0 flex-1">
            <Link to="/" onClick={onClose} className="font-sans text-sm font-bold text-white hover:text-brand-300">
              Architect Guide
            </Link>
            <p className="text-[10px] text-slate-500">52-Week Program</p>
          </div>
        </div>

        <button
          type="button"
          onClick={onSearchClick}
          className="mx-3 mt-3 flex items-center gap-2 rounded-lg border border-surface-800 bg-surface-800/50 px-3 py-2 text-sm text-slate-400 transition hover:border-slate-600 hover:text-white"
        >
          <Search className="h-4 w-4" />
          <span className="flex-1 text-left">Search...</span>
          <kbd className="rounded bg-surface-900 px-1.5 text-[10px] text-slate-500">⌘K</kbd>
        </button>

        <div className="mx-3 mt-3 grid grid-cols-4 gap-1 rounded-lg bg-surface-800/60 p-1">
          {TABS.map(({ id, label, icon: Icon }) => (
            <button
              key={id}
              type="button"
              onClick={() => setActiveTab(id)}
              className={`flex flex-col items-center gap-0.5 rounded-md px-1 py-2 text-[10px] font-medium transition ${
                activeTab === id ? 'bg-brand-600 text-white' : 'text-slate-400 hover:text-white'
              }`}
            >
              <Icon className="h-4 w-4" />
              {label}
            </button>
          ))}
        </div>

        <nav className="flex-1 overflow-y-auto px-3 py-3 scrollbar-thin">
          {activeTab === 'start' && (
            <div className="space-y-0.5">
              {categorized.start.items.map((item) => (
                <SimpleLink key={item.path} item={item} onNavigate={onClose} />
              ))}
            </div>
          )}

          {activeTab === 'weeks' && (
            <div>
              <input
                type="search"
                placeholder="Filter weeks..."
                value={weekFilter}
                onChange={(e) => setWeekFilter(e.target.value)}
                className="mb-3 w-full rounded-lg border border-surface-800 bg-surface-800/40 px-3 py-2 text-sm text-white placeholder:text-slate-500 focus:border-brand-500 focus:outline-none"
              />
              {filteredMonths.map((month, i) => (
                <MonthBlock
                  key={month.title}
                  month={month}
                  defaultOpen={i === activeMonthIndex || weekFilter.length > 0}
                  onNavigate={onClose}
                />
              ))}
            </div>
          )}

          {activeTab === 'library' && (
            <div>
              {categorized.library.map((section) => (
                <LibrarySection key={section.title} section={section} onNavigate={onClose} />
              ))}
            </div>
          )}

          {activeTab === 'program' && (
            <div className="space-y-0.5">
              {categorized.program.items.map((item) => (
                <SimpleLink key={item.path} item={item} onNavigate={onClose} />
              ))}
            </div>
          )}
        </nav>

        <div className="border-t border-surface-800 px-4 py-3">
          <p className="text-[10px] leading-relaxed text-slate-600">
            Tip: open a week, then use the section bar (Theory, Labs…) at the top of the page.
          </p>
        </div>
      </aside>
    </>
  )
}
