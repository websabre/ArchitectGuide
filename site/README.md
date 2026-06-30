# Architect Guide — Static Site

React + Vite + Tailwind static site for the Solution Architect Master Program curriculum.

## Quick Start

```bash
cd site
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173).

## Build for Production

```bash
cd site
npm run build
npm run preview
```

Output: `site/dist/` — deploy anywhere static files are hosted.

## Deploy

### GitHub Pages

1. Build: `cd site && npm run build`
2. Deploy `site/dist/` to `gh-pages` branch or use GitHub Actions
3. Site uses **HashRouter** — works without server rewrite rules

### Netlify / Vercel / Azure Static Web Apps

- **Build command:** `cd site && npm install && npm run build`
- **Publish directory:** `site/dist`
- No special redirects needed (hash-based routing)

### Azure Static Web Apps (example)

```yaml
app_location: site
output_location: dist
app_build_command: npm run build
```

## How It Works

1. `scripts/prepare_site.py` copies all `.md` files to `site/public/content/`
2. Generates `site/src/data/navigation.json` from folder structure
3. React app fetches markdown at runtime and renders with typography + Mermaid

Re-run automatically via `predev` and `prebuild` npm hooks.

## Tech Stack

- **Vite** — fast builds, easy static export
- **React 18** + **React Router** (HashRouter for zero-config deploy)
- **Tailwind CSS** + **@tailwindcss/typography** — reading-optimized prose
- **DM Sans** (UI) + **Source Serif 4** (body) + **JetBrains Mono** (code)
- **react-markdown** + **remark-gfm** — tables, GFM support
- **Mermaid** — architecture diagrams from curriculum

## Fonts & Typography

- Body prose: Source Serif 4 at 17px / 1.75 line-height
- Headings & UI: DM Sans with tight tracking
- Max content width: ~72ch for comfortable reading
- Consistent spacing via Tailwind scale
