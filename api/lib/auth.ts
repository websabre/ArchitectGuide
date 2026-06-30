import type { VercelRequest } from '@vercel/node'

export function checkAdminAuth(req: VercelRequest): boolean {
  const password = process.env.ADMIN_PASSWORD
  if (!password) return false

  const auth = req.headers.authorization
  if (!auth?.startsWith('Bearer ')) return false
  const token = auth.slice(7)
  return token === password
}

export function loginValid(body: unknown): boolean {
  const password = process.env.ADMIN_PASSWORD
  if (!password || !body || typeof body !== 'object') return false
  const p = (body as { password?: string }).password
  return p === password
}
