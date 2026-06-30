import { useEffect, useRef, useId } from 'react'
import mermaid from 'mermaid'

mermaid.initialize({
  startOnLoad: false,
  theme: 'neutral',
  securityLevel: 'loose',
  fontFamily: 'DM Sans, system-ui, sans-serif',
})

interface MermaidDiagramProps {
  chart: string
}

export function MermaidDiagram({ chart }: MermaidDiagramProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const id = useId().replace(/:/g, '')

  useEffect(() => {
    const el = containerRef.current
    if (!el) return

    let cancelled = false

    const render = async () => {
      try {
        const { svg } = await mermaid.render(`mermaid-${id}`, chart.trim())
        if (!cancelled) el.innerHTML = svg
      } catch {
        if (!cancelled) {
          el.innerHTML = `<pre class="text-sm text-red-600 p-4">${chart}</pre>`
        }
      }
    }

    render()
    return () => {
      cancelled = true
    }
  }, [chart, id])

  return <div ref={containerRef} className="mermaid-diagram" aria-label="Architecture diagram" />
}
