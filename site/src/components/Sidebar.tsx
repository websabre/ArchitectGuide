import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { ChevronDown, ChevronRight, BookOpen } from 'lucide-react'
import type { NavItem, NavSection } from '../lib/content'

interface SidebarProps {
  sections: NavSection[]
  mobileOpen: boolean
  onClose: () => void
}

function isPathActive(current: string, target: string): boolean {
  return current === target || current === `${target}/README`
}

function isTreeOpen(item: NavItem, pathname: string): boolean {
  if (isPathActive(pathname, item.path)) return true
  return (
    item.children?.some(
      (c) =>
        isPathActive(pathname, c.path) ||
        c.children?.some((cc) => isPathActive(pathname, cc.path)),
    ) ?? false
  )
}

function NavTreeItem({ item, depth = 0, onNavigate }: { item: NavItem; depth?: number; onNavigate: () => void }) {
  const location = useLocation()
  const [open, setOpen] = useState(() => isTreeOpen(item, location.pathname))
  const isActive = isPathActive(location.pathname, item.path)
  const hasChildren = item.children && item.children.length > 0
  const paddingLeft = 12 + depth * 12

  if (!hasChildren) {
    return (
      <Link
        to={item.path}
        onClick={onNavigate}
        style={{ paddingLeft }}
        className={`nav-link truncate ${isActive ? 'nav-link-active' : ''}`}
      >
        {item.title}
      </Link>
    )
  }

  return (
    <div>
      <div className="flex items-center gap-0.5" style={{ paddingLeft }}>
        <button
          type="button"
          onClick={() => setOpen(!open)}
          className="shrink-0 rounded p-1 text-slate-500 hover:bg-surface-800 hover:text-slate-300"
          aria-label={open ? 'Collapse' : 'Expand'}
        >
          {open ? <ChevronDown className="h-3.5 w-3.5" /> : <ChevronRight className="h-3.5 w-3.5" />}
        </button>
        <Link
          to={item.path}
          onClick={onNavigate}
          className={`nav-link min-w-0 flex-1 truncate ${isActive ? 'nav-link-active' : ''}`}
        >
          {item.title}
        </Link>
      </div>
      {open && (
        <div className="mt-0.5 space-y-0.5">
          {item.children!.map((child) => (
            <NavTreeItem key={`${child.path}-${child.title}`} item={child} depth={depth + 1} onNavigate={onNavigate} />
          ))}
        </div>
      )}
    </div>
  )
}

export function Sidebar({ sections, mobileOpen, onClose }: SidebarProps) {
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
        <div className="flex h-16 shrink-0 items-center gap-3 border-b border-surface-800 px-5">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-brand-600">
            <BookOpen className="h-5 w-5 text-white" />
          </div>
          <div>
            <Link to="/" onClick={onClose} className="font-sans text-sm font-bold text-white hover:text-brand-300">
              Architect Guide
            </Link>
            <p className="text-xs text-slate-500">52-Week Program</p>
          </div>
        </div>

        <nav className="flex-1 overflow-y-auto px-3 py-4 scrollbar-thin">
          {sections.map((section) => (
            <div key={section.title} className="mb-6">
              <h3 className="mb-2 px-3 text-[11px] font-semibold uppercase tracking-wider text-slate-500">
                {section.title}
              </h3>
              <div className="space-y-0.5">
                {section.items.map((item) => (
                  <NavTreeItem key={`${item.path}-${item.title}`} item={item} onNavigate={onClose} />
                ))}
              </div>
            </div>
          ))}
        </nav>

        <div className="border-t border-surface-800 px-5 py-4">
          <p className="text-xs text-slate-500">Solution Architect Master Program</p>
        </div>
      </aside>
    </>
  )
}
