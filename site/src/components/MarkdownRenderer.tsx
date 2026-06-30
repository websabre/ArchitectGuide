import { useMemo } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeSlug from 'rehype-slug'
import type { Components } from 'react-markdown'
import { MermaidDiagram } from './MermaidDiagram'
import { Link, useLocation } from 'react-router-dom'
import { resolveRelativeLink } from '../lib/content'

interface MarkdownRendererProps {
  content: string
}

export function MarkdownRenderer({ content }: MarkdownRendererProps) {
  const location = useLocation()
  const routePath = location.pathname

  const components: Components = useMemo(
    () => ({
      a: ({ href, children, ...props }) => {
        const target = href ? resolveRelativeLink(href, routePath) : href
        if (target?.startsWith('/doc/') || target === '/') {
          return (
            <Link to={target} className="text-brand-600 hover:text-brand-700" {...props}>
              {children}
            </Link>
          )
        }
        if (target?.startsWith('http')) {
          return (
            <a href={target} target="_blank" rel="noopener noreferrer" {...props}>
              {children}
            </a>
          )
        }
        return (
          <a href={target} {...props}>
            {children}
          </a>
        )
      },
      pre: ({ children, ...props }) => {
        const child = Array.isArray(children) ? children[0] : children
        if (
          child &&
          typeof child === 'object' &&
          'props' in child &&
          child.props?.className?.includes('language-mermaid')
        ) {
          const code = String(child.props.children).replace(/\n$/, '')
          return <MermaidDiagram chart={code} />
        }
        return (
          <pre className="overflow-x-auto rounded-xl text-sm" {...props}>
            {children}
          </pre>
        )
      },
      table: ({ children, ...props }) => (
        <div className="my-6 overflow-x-auto rounded-xl border border-slate-200 shadow-sm">
          <table className="min-w-full divide-y divide-slate-200" {...props}>
            {children}
          </table>
        </div>
      ),
      th: ({ children, ...props }) => (
        <th className="bg-slate-50 px-4 py-3 text-left text-sm font-semibold text-slate-900" {...props}>
          {children}
        </th>
      ),
      td: ({ children, ...props }) => (
        <td className="px-4 py-3 text-sm text-slate-700" {...props}>
          {children}
        </td>
      ),
    }),
    [routePath],
  )

  return (
    <article className="prose-content">
      <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeSlug]} components={components}>
        {content}
      </ReactMarkdown>
    </article>
  )
}
