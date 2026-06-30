import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { trackPageView } from '../lib/analytics'

/** Records page views on route change (skips /admin). */
export function AnalyticsTracker() {
  const location = useLocation()

  useEffect(() => {
    const path = location.pathname + location.search + location.hash
    if (!path.startsWith('/admin')) {
      trackPageView(path || '/')
    }
  }, [location])

  return null
}
