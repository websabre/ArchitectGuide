import { Link } from 'react-router-dom'
import {
  BookOpen,
  Calendar,
  Target,
  Cloud,
  Boxes,
  Brain,
  ArrowRight,
  GraduationCap,
} from 'lucide-react'

const phases = [
  { month: 1, title: '.NET Foundation', weeks: '1–4', icon: BookOpen, color: 'bg-blue-500' },
  { month: 2, title: 'Data & Algorithms', weeks: '5–8', icon: Target, color: 'bg-violet-500' },
  { month: 3, title: 'Azure Core', weeks: '9–12', icon: Cloud, color: 'bg-sky-500' },
  { month: 4, title: 'Azure Deep Dive', weeks: '13–16', icon: Cloud, color: 'bg-cyan-500' },
  { month: 5, title: 'AWS & Multi-Cloud', weeks: '17–20', icon: Cloud, color: 'bg-orange-500' },
  { month: 6, title: 'Distributed Systems', weeks: '21–24', icon: Boxes, color: 'bg-indigo-500' },
  { month: 7, title: 'Containers & K8s', weeks: '25–28', icon: Boxes, color: 'bg-purple-500' },
  { month: 8, title: 'DevOps', weeks: '29–32', icon: Target, color: 'bg-emerald-500' },
  { month: 9, title: 'System Design', weeks: '33–36', icon: Target, color: 'bg-rose-500' },
  { month: 10, title: 'AI Architecture', weeks: '37–40', icon: Brain, color: 'bg-fuchsia-500' },
  { month: 11, title: 'Enterprise', weeks: '41–44', icon: GraduationCap, color: 'bg-amber-500' },
  { month: 12, title: 'Interview & Graduation', weeks: '45–52', icon: GraduationCap, color: 'bg-brand-600' },
]

export function HomePage() {
  return (
    <div className="-mx-4 -mt-4 lg:-mx-10 lg:-mt-8">
      {/* Hero */}
      <section className="relative overflow-hidden bg-gradient-to-br from-surface-900 via-brand-950 to-surface-900 px-6 py-16 text-white lg:px-12 lg:py-24">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-brand-600/20 via-transparent to-transparent" />
        <div className="relative mx-auto max-w-3xl">
          <p className="mb-4 inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-xs font-medium text-brand-200 backdrop-blur">
            <Calendar className="h-3.5 w-3.5" />
            2026 Edition · 52 Weeks
          </p>
          <h1 className="mb-6 font-sans text-4xl font-bold leading-tight tracking-tight lg:text-5xl">
            Solution Architect
            <br />
            <span className="text-brand-300">Master Program</span>
          </h1>
          <p className="mb-8 max-w-2xl font-serif text-lg leading-relaxed text-slate-300">
            From senior .NET developer to solution architect, cloud architect, and staff engineer.
            Structured theory, labs, assessments, and 3,000+ interview questions — built for production
            architecture thinking.
          </p>
          <div className="flex flex-wrap gap-3">
            <Link
              to="/doc/weeks/week-01/README"
              className="inline-flex items-center gap-2 rounded-xl bg-brand-500 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-brand-500/25 transition hover:bg-brand-400"
            >
              Start Week 01
              <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              to="/doc/SYLLABUS"
              className="inline-flex items-center gap-2 rounded-xl border border-white/20 bg-white/5 px-5 py-3 text-sm font-medium text-white backdrop-blur transition hover:bg-white/10"
            >
              View Syllabus
            </Link>
            <Link
              to="/doc/docs/getting-started/how-to-use-this-guide"
              className="inline-flex items-center gap-2 rounded-xl border border-white/20 px-5 py-3 text-sm font-medium text-slate-300 transition hover:text-white"
            >
              How to Use
            </Link>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="border-b border-slate-200 bg-white px-6 py-10 lg:px-12">
        <div className="mx-auto grid max-w-4xl grid-cols-2 gap-6 sm:grid-cols-4">
          {[
            { label: 'Weeks', value: '52' },
            { label: 'Interview Q&A', value: '3,000+' },
            { label: 'Case Studies', value: '40+' },
            { label: 'Labs', value: '52' },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <p className="font-sans text-3xl font-bold text-brand-600">{stat.value}</p>
              <p className="mt-1 text-sm text-slate-500">{stat.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Phase grid */}
      <section className="px-6 py-12 lg:px-12 lg:py-16">
        <div className="mx-auto max-w-4xl">
          <h2 className="mb-2 font-sans text-2xl font-bold text-slate-900">12-Month Journey</h2>
          <p className="mb-8 font-serif text-slate-600">
            Four weeks per phase. Each week includes theory, diagrams, labs, exercises, interview Q&A,
            case studies, and assessments.
          </p>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {phases.map((phase) => {
              const weekNum = (phase.month - 1) * 4 + 1
              const Icon = phase.icon
              return (
                <Link
                  key={phase.month}
                  to={`/doc/weeks/week-${String(weekNum).padStart(2, '0')}/README`}
                  className="group flex items-start gap-4 rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition hover:border-brand-300 hover:shadow-md"
                >
                  <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-lg ${phase.color} text-white`}>
                    <Icon className="h-5 w-5" />
                  </div>
                  <div>
                    <p className="text-xs font-medium text-slate-500">Month {phase.month}</p>
                    <p className="font-sans font-semibold text-slate-900 group-hover:text-brand-600">
                      {phase.title}
                    </p>
                    <p className="text-xs text-slate-500">Weeks {phase.weeks}</p>
                  </div>
                </Link>
              )
            })}
          </div>
        </div>
      </section>

      {/* Quick links */}
      <section className="border-t border-slate-200 bg-slate-50 px-6 py-12 lg:px-12">
        <div className="mx-auto grid max-w-4xl gap-4 sm:grid-cols-3">
          {[
            { title: 'Curriculum Map', path: '/doc/CURRICULUM-MAP', desc: '52-week topic reference' },
            { title: 'Interview Prep', path: '/doc/interview-prep/README', desc: 'Top 50 & mock sessions' },
            { title: 'Study Plan', path: '/doc/STUDY-PLAN-12-MONTHS', desc: 'Monthly deliverables' },
          ].map((link) => (
            <Link
              key={link.path}
              to={link.path}
              className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-brand-300 hover:shadow-md"
            >
              <p className="font-sans font-semibold text-slate-900">{link.title}</p>
              <p className="mt-1 text-sm text-slate-500">{link.desc}</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  )
}
