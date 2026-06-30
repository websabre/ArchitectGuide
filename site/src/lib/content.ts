export interface NavItem {
  title: string
  path: string
  children?: NavItem[]
}

export interface NavSection {
  title: string
  items: NavItem[]
}

export interface NavigationData {
  sections: NavSection[]
}

const README_SUFFIX = '/README'

function stripReadmeSuffix(path: string): string {
  return path.endsWith(README_SUFFIX) ? path.slice(0, -README_SUFFIX.length) : path
}

export function normalizeDocPath(path: string): string {
  let p = path.replace(/^\/doc\//, '').replace(/^\//, '')
  if (p.endsWith('.md')) p = p.slice(0, -3)
  return stripReadmeSuffix(p)
}

/** Build ordered list of content file paths to try for a route */
export function contentCandidates(routePath: string): string[] {
  const raw = routePath.replace(/^\/doc\//, '').replace(/^\//, '')
  const base = raw.endsWith('.md') ? raw.slice(0, -3) : raw
  const folder = stripReadmeSuffix(base)

  // Always try README.md first — avoids Vite SPA fallback returning index.html for missing .md
  return [`${folder}/README.md`, `${folder}.md`]
}

function contentFetchUrl(rel: string): string {
  const base = import.meta.env.BASE_URL || '/'
  if (base.startsWith('http')) {
    return `${base.replace(/\/?$/, '/')}content/${rel}`
  }
  const pathPrefix = base === './'
    ? window.location.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '')
    : base.replace(/\/$/, '')
  return `${window.location.origin}${pathPrefix}/content/${rel}`
}

function isHtmlPayload(text: string, contentType: string | null): boolean {
  if (contentType?.includes('text/html')) return true
  const trimmed = text.trimStart().slice(0, 20).toLowerCase()
  return trimmed.startsWith('<!doctype') || trimmed.startsWith('<html')
}

export async function fetchMarkdown(routePath: string): Promise<string> {
  const candidates = contentCandidates(routePath)

  for (const rel of candidates) {
    const url = contentFetchUrl(rel)
    const res = await fetch(url)
    if (!res.ok) continue

    const text = await res.text()
    if (isHtmlPayload(text, res.headers.get('content-type'))) continue

    return text
  }

  throw new Error(`Content not found: ${routePath}`)
}

const SECTION_FOLDERS = new Set([
  'theory', 'diagrams', 'labs', 'exercises', 'interview-questions',
  'case-studies', 'assessments', 'modules', 'docs', 'program',
  'interview-prep', 'getting-started', 'cross-cutting', 'reference',
])

/** Directory containing the current markdown file (for resolving relative links) */
export function contentBaseDir(routePath: string): string {
  let p = routePath.replace(/^\/doc\//, '').replace(/^\//, '')
  if (p.endsWith('.md')) p = p.slice(0, -3)
  p = stripReadmeSuffix(p)

  const segments = p.split('/').filter(Boolean)
  if (segments.length === 0) return ''

  const last = segments[segments.length - 1]
  const isDirectoryRoute =
    /^week-\d{2}$/.test(last) ||
    SECTION_FOLDERS.has(last) ||
    routePath.endsWith('/README')

  if (!isDirectoryRoute) {
    return segments.slice(0, -1).join('/')
  }
  return p
}

export function resolveRelativeLink(href: string, routePath: string): string {
  if (href.startsWith('http://') || href.startsWith('https://') || href.startsWith('#')) {
    return href
  }
  if (href.startsWith('/doc/') || href === '/') {
    return href
  }

  const currentDir = contentBaseDir(routePath)

  let resolved = href
  if (!href.startsWith('/')) {
    const parts = [...(currentDir ? currentDir.split('/') : []), ...href.split('/')]
    const normalized: string[] = []
    for (const part of parts) {
      if (part === '..') normalized.pop()
      else if (part !== '.' && part !== '') normalized.push(part)
    }
    resolved = normalized.join('/')
  } else {
    resolved = href.replace(/^\//, '')
  }

  if (resolved.endsWith('.md')) resolved = resolved.slice(0, -3)
  resolved = stripReadmeSuffix(resolved)

  return `/doc/${resolved}`
}

export function rewriteMarkdownLinks(markdown: string, routePath: string): string {
  return markdown.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, text, href) => {
    const resolved = resolveRelativeLink(href, routePath)
    if (resolved === href) return match
    return `[${text}](${resolved})`
  })
}

export function titleFromPath(path: string): string {
  const segment = path.split('/').pop() || 'Document'
  return segment
    .replace(/-/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase())
}

export function flattenNav(sections: NavSection[]): NavItem[] {
  const result: NavItem[] = []
  const seen = new Set<string>()
  const walk = (items: NavItem[]) => {
    for (const item of items) {
      if (!seen.has(item.path)) {
        seen.add(item.path)
        result.push(item)
      }
      if (item.children) walk(item.children)
    }
  }
  for (const section of sections) walk(section.items)
  return result
}
