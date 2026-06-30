import type { NavItem, NavSection } from './content'

export type NavTab = 'start' | 'weeks' | 'library' | 'program'

export interface CategorizedNav {
  start: NavSection
  months: NavSection[]
  library: NavSection[]
  program: NavSection
}

const LIBRARY_TITLES = new Set(['Modules', 'Interview Prep', 'Documentation', 'Resources'])

export function categorizeNavigation(sections: NavSection[]): CategorizedNav {
  const start = sections.find((s) => s.title === 'Start') ?? { title: 'Start', items: [] }
  const months = sections.filter((s) => s.title.startsWith('Month '))
  const library = sections.filter((s) => LIBRARY_TITLES.has(s.title))
  const program = sections.find((s) => s.title === 'Program') ?? { title: 'Program', items: [] }
  return { start, months, library, program }
}

export function parseWeekFromPath(pathname: string): string | null {
  const match = pathname.match(/\/doc\/weeks\/(week-\d{2})/)
  return match ? match[1] : null
}

export function findWeekItem(months: NavSection[], weekId: string): NavItem | null {
  for (const month of months) {
    const week = month.items.find((i) => i.path.includes(`/${weekId}`))
    if (week) return week
  }
  return null
}

/** Flatten week sections for sub-nav (Theory, Labs, etc.) — skip deep interview file trees */
export function weekSectionLinks(week: NavItem): NavItem[] {
  if (!week.children) return []
  return week.children.map((child) => ({
    title: child.title,
    path: child.path,
    // keep one level only in subnav
  }))
}

export function isPathActive(current: string, target: string): boolean {
  return current === target || current === `${target}/README`
}

export function isWeekPathActive(pathname: string, sectionPath: string): boolean {
  if (isPathActive(pathname, sectionPath)) return true
  return pathname.startsWith(sectionPath + '/')
}

export function detectActiveTab(pathname: string): NavTab {
  if (pathname === '/') return 'start'
  if (pathname.includes('/weeks/week-')) return 'weeks'
  if (pathname.includes('/program/phase-')) return 'program'
  return 'library'
}
