import { useState, useEffect, useCallback } from 'react'
import { Outlet, useLocation } from 'react-router-dom'
import { Sidebar } from './Sidebar'
import { Header } from './Header'
import { SearchDialog } from './SearchDialog'
import navigationData from '../data/navigation.json'
import type { NavigationData } from '../lib/content'
import { titleFromPath } from '../lib/content'

export function Layout() {
  const [mobileOpen, setMobileOpen] = useState(false)
  const [searchOpen, setSearchOpen] = useState(false)
  const location = useLocation()
  const nav = navigationData as NavigationData

  const pageTitle =
    location.pathname === '/'
      ? undefined
      : titleFromPath(location.pathname.replace(/^\/doc\//, ''))

  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault()
      setSearchOpen(true)
    }
  }, [])

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [handleKeyDown])

  useEffect(() => {
    setMobileOpen(false)
    window.scrollTo(0, 0)
  }, [location.pathname])

  return (
    <div className="flex min-h-screen">
      <Sidebar sections={nav.sections} mobileOpen={mobileOpen} onClose={() => setMobileOpen(false)} />

      <div className="flex min-w-0 flex-1 flex-col">
        <Header
          title={pageTitle}
          onMenuClick={() => setMobileOpen(true)}
          onSearchClick={() => setSearchOpen(true)}
        />

        <main className="flex-1">
          <div className="mx-auto max-w-4xl px-4 py-8 lg:px-10 lg:py-12">
            <Outlet />
          </div>
        </main>

        <footer className="border-t border-slate-200 bg-white px-4 py-6 lg:px-10">
          <p className="text-center text-sm text-slate-500">
            Solution Architect Master Program · 52 weeks · .NET · Azure · AWS · System Design
          </p>
        </footer>
      </div>

      <SearchDialog open={searchOpen} onClose={() => setSearchOpen(false)} />
    </div>
  )
}
