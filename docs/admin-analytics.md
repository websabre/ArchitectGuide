# Admin Analytics Setup

Password-protected dashboard at **`/admin`** on your deployed site.

## 1. Vercel KV (storage)

1. [Vercel Dashboard](https://vercel.com) → your project → **Storage**
2. **Create Database** → **KV** → connect to `architectguide`
3. Env vars `KV_REST_API_URL` and `KV_REST_API_TOKEN` are added automatically

## 2. Admin password

**Settings → Environment Variables** → add:

| Name | Value |
|------|--------|
| `ADMIN_PASSWORD` | A strong secret (used for login + API auth) |

Redeploy after adding variables.

## 3. Access

Open: `https://architectguide.vercel.app/admin`

Sign in with `ADMIN_PASSWORD`.

## What is tracked

| Field | Source |
|-------|--------|
| Page path | Client route changes |
| Session ID | Anonymous UUID in `localStorage` |
| IP address | `x-forwarded-for` |
| City / country | Vercel geo headers (`x-vercel-ip-city`, etc.) |
| Referrer, user agent | Browser |
| Timestamp | Server |

Last **10,000** events kept in KV.

## Local development

```bash
# From repo root — runs site + API
npx vercel dev
```

Set `.env.local` with `ADMIN_PASSWORD` and KV vars (or pull from Vercel: `vercel env pull`).

## Privacy

Inform visitors if required by your jurisdiction (GDPR, etc.). IP collection may need a privacy notice on the public site.
