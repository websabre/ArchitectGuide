import { Link, useLocation } from 'react-router-dom'
import {
  BookOpen,
  Layers,
  FlaskConical,
  PenLine,
  MessageCircleQuestion,
  FileText,
  ClipboardCheck,
  AlertTriangle,
  LayoutGrid,
} from 'lucide-react'
import type { NavSection } from '../lib/content'
import { isWeekPathActive, weekSectionLinks, findWeekItem, parseWeekFromPath } from '../lib/nav-helpers'

const SECTION_ICONS: Record<string, typeof BookOpen> = {
  Theory: BookOpen,
  Diagrams: LayoutGrid,
  Labs: FlaskConical,
  Exercises: PenLine,
  'Interview Q&A': MessageCircleQuestion,
  'Case Studies': FileText,
  Assessments: ClipboardCheck,
  'Common Mistakes': AlertTriangle,
}

interface WeekSubnavProps {
  months: NavSection[]
}

export function WeekSubnav({ months }: WeekSubnavProps) {
  const location = useLocation()
  const weekId = parseWeekFromPath(location.pathname)
  if (!weekId) return null

  const week = findWeekItem(months, weekId)
  if (!week) return null

  const sections = weekSectionLinks(week)
  const weekLabel = week.title.replace(/^Week \d+ — /, '')

  return (
    <div className="sticky top-14 z-20 border-b border-slate-200 bg-white/95 backdrop-blur-md">
      <div className="mx-auto max-w-4xl px-4 lg:px-10">
        <div className="flex items-center gap-3 py-2">
          <Link
            to={week.path}
            className="hidden shrink-0 rounded-lg bg-brand-50 px-2.5 py-1 text-xs font-semibold text-brand-700 hover:bg-brand-100 sm:block"
          >
            {weekId.replace('week-', 'W')}
          </Link>
          <span className="hidden truncate text-xs text-slate-500 sm:block">{weekLabel}</span>
          <span className="hidden text-slate-300 sm:inline">|</span>
          <nav
            className="flex flex-1 gap-1 overflow-x-auto pb-0.5 scrollbar-thin"
            aria-label="Week sections"
          >
            {sections.map((section) => {
              const Icon = SECTION_ICONS[section.title] ?? Layers
              const active = isWeekPathActive(location.pathname, section.path)
              return (
                <Link
                  key={section.path}
                  to={section.path}
                  className={`flex shrink-0 items-center gap-1.5 rounded-lg px-2.5 py-1.5 text-xs font-medium transition ${
                    active
                      ? 'bg-brand-600 text-white shadow-sm'
                      : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                  }`}
                >
                  <Icon className="h-3.5 w-3.5" />
                  <span className="whitespace-nowrap">{section.title}</span>
                </Link>
              )
            })}
          </nav>
        </div>
      </div>
    </div>
  )
}
