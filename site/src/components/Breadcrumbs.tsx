import { Link } from 'react-router-dom'
import { ChevronRight } from 'lucide-react'

interface BreadcrumbsProps {
  path: string
}

export function Breadcrumbs({ path }: BreadcrumbsProps) {
  if (!path || path === '/') return null

  const segments = path.replace(/^\/doc\//, '').split('/').filter(Boolean)
  const crumbs = segments.map((seg, i) => {
    const fullPath = '/doc/' + segments.slice(0, i + 1).join('/')
    const label = seg
      .replace(/^week-(\d+)$/, 'Week $1')
      .replace(/-/g, ' ')
      .replace(/\b\w/g, (c) => c.toUpperCase())
    return { label, path: fullPath }
  })

  return (
    <nav aria-label="Breadcrumb" className="mb-6 flex flex-wrap items-center gap-1 text-sm text-slate-500">
      <Link to="/" className="hover:text-brand-600">
        Home
      </Link>
      {crumbs.map((crumb, i) => (
        <span key={crumb.path} className="flex items-center gap-1">
          <ChevronRight className="h-3.5 w-3.5 text-slate-300" />
          {i === crumbs.length - 1 ? (
            <span className="font-medium text-slate-700">{crumb.label}</span>
          ) : (
            <Link to={crumb.path} className="hover:text-brand-600">
              {crumb.label}
            </Link>
          )}
        </span>
      ))}
    </nav>
  )
}
