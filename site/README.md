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

### GitHub Pages (GitHub Actions)

**One-time repo setup** (required — fixes `Failed to create deployment (status: 404)`):

1. Open **Settings → Pages** on your GitHub repo
2. Under **Build and deployment → Source**, select **GitHub Actions** (not “Deploy from a branch”)
3. Save, then re-run the **Deploy Site** workflow (Actions tab → Deploy Site → Re-run all jobs)

The workflow (`.github/workflows/deploy-site.yml`) builds `site/dist` on push to `main` and deploys via OIDC.

Live URL after first successful deploy: `https://<user>.github.io/<repo>/`

Site uses **HashRouter** — no server rewrite rules needed.

### Vercel (CLI)

**Important:** Run `vercel` from the **repo root** (`ArchitectGuide/`), not from `site/`.

```bash
cd /path/to/ArchitectGuide
vercel link
vercel --prod
```

`vercel.json` at repo root runs `cd site && npm run build` and publishes `site/dist/`.

**Admin analytics + KV storage:** see [docs/vercel-kv-setup.md](../docs/vercel-kv-setup.md) and [docs/admin-analytics.md](../docs/admin-analytics.md).

### Netlify / Azure Static Web Apps

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
- **React 18** + **React Router** (BrowserRouter; Vercel SPA rewrites in root `vercel.json`)
- **Tailwind CSS** + **@tailwindcss/typography** — reading-optimized prose
- **DM Sans** (UI) + **Source Serif 4** (body) + **JetBrains Mono** (code)
- **react-markdown** + **remark-gfm** — tables, GFM support
- **Mermaid** — architecture diagrams from curriculum

## Fonts & Typography

- Body prose: Source Serif 4 at 17px / 1.75 line-height
- Headings & UI: DM Sans with tight tracking
- Max content width: ~72ch for comfortable reading
- Consistent spacing via Tailwind scale
