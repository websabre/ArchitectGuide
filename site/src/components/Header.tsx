import { Link } from 'react-router-dom'
import { Menu, Search, Home } from 'lucide-react'

interface HeaderProps {
  title?: string
  onMenuClick: () => void
  onSearchClick: () => void
}

export function Header({ title, onMenuClick, onSearchClick }: HeaderProps) {
  return (
    <header className="sticky top-0 z-30 border-b border-slate-200/80 bg-white/90 backdrop-blur-md">
      <div className="flex h-14 items-center gap-4 px-4 lg:px-8">
        <button
          type="button"
          onClick={onMenuClick}
          className="rounded-lg p-2 text-slate-600 hover:bg-slate-100 lg:hidden"
          aria-label="Open menu"
        >
          <Menu className="h-5 w-5" />
        </button>

        <div className="flex min-w-0 flex-1 items-center gap-3">
          <Link
            to="/"
            className="hidden rounded-lg p-2 text-slate-500 hover:bg-slate-100 hover:text-brand-600 lg:block"
            aria-label="Home"
          >
            <Home className="h-4 w-4" />
          </Link>
          {title && (
            <h1 className="truncate font-sans text-base font-semibold text-slate-900 lg:text-lg">{title}</h1>
          )}
        </div>

        <button
          type="button"
          onClick={onSearchClick}
          className="flex items-center gap-2 rounded-lg border border-slate-200 bg-slate-50 px-3 py-1.5 text-sm text-slate-500 transition hover:border-slate-300 hover:bg-white"
        >
          <Search className="h-4 w-4" />
          <span className="hidden sm:inline">Search</span>
          <kbd className="hidden rounded bg-white px-1.5 py-0.5 text-[10px] font-medium text-slate-400 shadow-sm sm:inline">
            ⌘K
          </kbd>
        </button>
      </div>
    </header>
  )
}
