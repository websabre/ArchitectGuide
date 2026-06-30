#!/usr/bin/env node
/**
 * Copy markdown content and generate navigation.json for the static site.
 * Run from site/ — curriculum root is one level up (full repo required on Vercel).
 */
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const SITE = path.resolve(__dirname, '..')
const ROOT = path.resolve(SITE, '..')
const CONTENT_OUT = path.join(SITE, 'public', 'content')
const NAV_OUT = path.join(SITE, 'src', 'data', 'navigation.json')

const WEEK_TOPICS = {
  1: 'C# Language Mastery', 2: '.NET Runtime & Ecosystem', 3: 'SOLID & Clean Architecture',
  4: 'Design Patterns', 5: 'Data Structures', 6: 'Algorithms & Complexity', 7: 'SQL Server',
  8: 'PostgreSQL', 9: 'Azure Fundamentals', 10: 'Azure Compute', 11: 'Azure Data Platform',
  12: 'Azure Identity', 13: 'Azure Networking', 14: 'Azure Security', 15: 'Azure Integration',
  16: 'Azure Capstone', 17: 'AWS Fundamentals', 18: 'AWS Compute', 19: 'AWS Data & VPC',
  20: 'Multi-Cloud', 21: 'Distributed Systems', 22: 'Microservices', 23: 'Domain-Driven Design',
  24: 'Microservices Capstone', 25: 'Docker & Containers', 26: 'Kubernetes Fundamentals',
  27: 'Kubernetes Advanced', 28: 'Linux for Architects', 29: 'DevOps Culture', 30: 'CI/CD Pipelines',
  31: 'Infrastructure as Code', 32: 'Observability', 33: 'System Design', 34: 'Scalability & Caching',
  35: 'Messaging & Events', 36: 'System Design Capstone', 37: 'AI/ML Architecture',
  38: 'RAG & Vector Search', 39: 'LLMOps', 40: 'AI Capstone', 41: 'Architecture Reviews',
  42: 'FinOps & DR', 43: 'Frontend Architecture', 44: 'Enterprise Case Studies',
  45: 'Interview Intensive I', 46: 'Interview Intensive II', 47: 'Interview Intensive III',
  48: 'Whiteboard Mocks I', 49: 'Whiteboard Mocks II', 50: 'Leadership I', 51: 'Leadership II',
  52: 'Graduation Capstone',
}

const PHASE_NAMES = {
  1: 'Month 1 — .NET Foundation', 2: 'Month 2 — Data & Algorithms', 3: 'Month 3 — Azure Core',
  4: 'Month 4 — Azure Deep Dive', 5: 'Month 5 — AWS & Multi-Cloud', 6: 'Month 6 — Distributed Systems',
  7: 'Month 7 — Containers & K8s', 8: 'Month 8 — DevOps', 9: 'Month 9 — System Design',
  10: 'Month 10 — AI Architecture', 11: 'Month 11 — Enterprise', 12: 'Month 12 — Interview & Graduation',
}

const WEEK_SECTIONS = [
  ['README.md', 'Overview'], ['theory', 'Theory'], ['diagrams', 'Diagrams'], ['labs', 'Labs'],
  ['exercises', 'Exercises'], ['interview-questions', 'Interview Q&A'], ['case-studies', 'Case Studies'],
  ['assessments', 'Assessments'],
]

const SKIP_DIRS = new Set(['.git', 'site', 'node_modules', '.cursor', 'scripts'])

function docPath(rel) {
  rel = rel.replace(/\\/g, '/')
  if (rel.endsWith('.md')) rel = rel.slice(0, -3)
  if (rel.endsWith('/README')) rel = rel.slice(0, -'/README'.length)
  return rel ? `/doc/${rel}` : '/doc'
}

function navItem(title, p, children) {
  const entry = { title, path: p }
  if (children?.length) entry.children = children
  return entry
}

function weekChildren(weekNum) {
  const weekDir = path.join(ROOT, `weeks/week-${String(weekNum).padStart(2, '0')}`)
  if (!fs.existsSync(weekDir)) return []
  const base = `weeks/week-${String(weekNum).padStart(2, '0')}`
  const children = []
  for (const [segment, label] of WEEK_SECTIONS) {
    if (segment.endsWith('.md')) {
      if (segment === 'README.md') continue
      if (fs.existsSync(path.join(weekDir, segment))) {
        children.push(navItem(label, docPath(`${base}/${segment.slice(0, -3)}`)))
      }
    } else {
      const folder = path.join(weekDir, segment)
      if (!fs.existsSync(folder)) continue
      const sub = []
      const sectionPath = docPath(`${base}/${segment}/README`)
      for (const name of fs.readdirSync(folder).filter((f) => f.endsWith('.md') && f !== 'README.md').sort()) {
        const stem = name.replace(/\.md$/, '')
        sub.push(navItem(stem.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), docPath(`${base}/${segment}/${stem}`)))
      }
      if (sub.length || fs.existsSync(path.join(folder, 'README.md'))) {
        children.push(navItem(label, sectionPath, sub.length ? sub : undefined))
      }
    }
  }
  if (fs.existsSync(path.join(weekDir, 'common-mistakes.md'))) {
    children.push(navItem('Common Mistakes', docPath(`${base}/common-mistakes`)))
  }
  return children
}

function scanDirNav(folder, basePath, maxDepth = 2) {
  if (!fs.existsSync(folder) || maxDepth <= 0) return []
  const items = []
  for (const name of fs.readdirSync(folder).sort()) {
    const child = path.join(folder, name)
    const stat = fs.statSync(child)
    if (stat.isDirectory() && !name.startsWith('.')) {
      const subPath = basePath ? `${basePath}/${name}` : name
      const readme = path.join(child, 'README.md')
      const mdFiles = fs.readdirSync(child).filter((f) => f.endsWith('.md') && f !== 'README.md').sort()
      const subItems = maxDepth > 1 ? scanDirNav(child, subPath, maxDepth - 1) : []
      if (fs.existsSync(readme)) {
        items.push(navItem(name.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), docPath(`${subPath}/README`), subItems.length ? subItems : undefined))
      } else if (mdFiles.length) {
        const fileChildren = mdFiles.map((f) => {
          const stem = f.replace(/\.md$/, '')
          return navItem(stem.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), docPath(`${subPath}/${stem}`))
        })
        items.push(navItem(name.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), fileChildren[0].path, fileChildren.length > 1 ? fileChildren : undefined))
      } else if (subItems.length) {
        items.push(navItem(name.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), subItems[0].path, subItems.length > 1 ? subItems : undefined))
      }
    } else if (name.endsWith('.md') && name !== 'README.md') {
      const stem = name.replace(/\.md$/, '')
      const rel = basePath ? `${basePath}/${stem}` : stem
      items.push(navItem(stem.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase()), docPath(rel)))
    }
  }
  return items
}

function buildNavigation() {
  const sections = [{
    title: 'Start',
    items: [
      navItem('Home', '/'),
      navItem('How to Use', docPath('docs/getting-started/how-to-use-this-guide')),
      navItem('Syllabus', docPath('SYLLABUS')),
      navItem('Curriculum Map', docPath('CURRICULUM-MAP')),
      navItem('12-Month Study Plan', docPath('STUDY-PLAN-12-MONTHS')),
    ],
  }]
  for (let phase = 1; phase <= 12; phase++) {
    const weekItems = []
    for (let w = (phase - 1) * 4 + 1; w <= phase * 4 && w <= 52; w++) {
      weekItems.push(navItem(`Week ${String(w).padStart(2, '0')} — ${WEEK_TOPICS[w] || `Week ${w}`}`, docPath(`weeks/week-${String(w).padStart(2, '0')}/README`), weekChildren(w)))
    }
    sections.push({ title: PHASE_NAMES[phase], items: weekItems })
  }
  sections.push({
    title: 'Program',
    items: Array.from({ length: 12 }, (_, i) => navItem(`Phase ${i + 1} Capstone`, docPath(`program/phase-${String(i + 1).padStart(2, '0')}-month-${String(i + 1).padStart(2, '0')}/capstone`))),
  })
  sections.push({ title: 'Modules', items: scanDirNav(path.join(ROOT, 'modules'), 'modules', 1) })
  sections.push({ title: 'Interview Prep', items: scanDirNav(path.join(ROOT, 'interview-prep'), 'interview-prep', 1) })
  sections.push({ title: 'Documentation', items: scanDirNav(path.join(ROOT, 'docs'), 'docs', 2) })
  sections.push({
    title: 'Resources',
    items: [navItem('Case Studies Index', docPath('case-studies/README')), navItem('Templates', docPath('templates/case-study-template'))],
  })
  return { sections }
}

function copyMarkdown() {
  if (fs.existsSync(CONTENT_OUT)) fs.rmSync(CONTENT_OUT, { recursive: true })
  fs.mkdirSync(CONTENT_OUT, { recursive: true })
  let count = 0
  function walk(dir) {
    for (const name of fs.readdirSync(dir)) {
      const full = path.join(dir, name)
      const relParts = path.relative(ROOT, full).split(path.sep)
      if (relParts.some((p) => SKIP_DIRS.has(p))) continue
      const stat = fs.statSync(full)
      if (stat.isDirectory()) walk(full)
      else if (name.endsWith('.md')) {
        const rel = path.relative(ROOT, full)
        const dest = path.join(CONTENT_OUT, rel)
        fs.mkdirSync(path.dirname(dest), { recursive: true })
        fs.copyFileSync(full, dest)
        count++
      }
    }
  }
  walk(ROOT)
  return count
}

function main() {
  if (!fs.existsSync(path.join(ROOT, 'weeks'))) {
    console.error('')
    console.error('ERROR: Curriculum folder not found at', path.join(ROOT, 'weeks'))
    console.error('')
    console.error('Vercel must deploy the FULL repo with Root Directory = site.')
    console.error('Run:  cd ArchitectGuide   (repo root, not site/)')
    console.error('      vercel link')
    console.error('      vercel --prod')
    console.error('')
    process.exit(1)
  }
  fs.mkdirSync(path.dirname(NAV_OUT), { recursive: true })
  fs.writeFileSync(NAV_OUT, JSON.stringify(buildNavigation(), null, 2))
  const count = copyMarkdown()
  console.log(`Navigation written to src/data/navigation.json`)
  console.log(`Copied ${count} markdown files to public/content`)
}

main()
