# AKD Project Detection Guide

This file teaches you how to analyze *any* AKD ecosystem frontend project and determine what Playwright configuration it needs. Read the project's actual files — don't assume based on project name.

---

## Step 1: Read these files first

Always read in this order before making any decisions:

1. `next.config.ts` (or `next.config.js`) — the most information-dense file
2. `package.json` — reveals port, existing scripts, installed deps
3. `src/app/` directory listing — reveals route structure and auth presence
4. `src/app/layout.tsx` or `src/app/providers.tsx` — reveals auth providers

---

## What to extract from `next.config.ts`

| Signal | What to look for | What it means |
|---|---|---|
| Static export | `output: 'export'` | No SSR; `next start` won't work — tests use `next dev` or a static server |
| API proxy | `rewrites()` returning `/api/:path*` → some destination | Note the destination host/port — that's the backend |
| Custom port | `server: { port: N }` or the dev script in package.json | Use that port for `BASE_URL` default |
| Trailing slash | `trailingSlash: true` | All `page.goto()` calls need trailing slashes |

---

## What to extract from `src/app/`

| Signal | What to look for | What it means |
|---|---|---|
| Auth required | A `login/` or `signin/` directory exists | Generate auth variant config + auth.setup.ts |
| Login URL | The name of the login route directory | Use that path in auth.setup.ts (e.g. `/login`, `/signin`) |
| Post-login destination | Read the login page component — find where it redirects after success | Use in auth.setup.ts to confirm login worked |
| Route structure | All directories under `src/app/` | Informs which pages are worth testing |

---

## What to extract from the login page component

If a login page exists, read `src/app/[login-route]/page.tsx` to find:

- **Email/username input**: look for `<input type="email">`, `getByLabel`, placeholder text, or `aria-label` — use the actual label text in auth selectors
- **Password input**: same approach
- **Submit button**: look for `<button type="submit">` or a button with sign-in copy — use the exact text
- **Error display**: this is critical — find the exact element that shows auth errors. Look for: conditional renders, `{error && ...}`, toast calls, or elements with `role="alert"`. Note the element type and any identifying attributes. **Do not assume `role="alert"` — read the actual markup.**
- **Redirect target**: find `router.push()` or `router.replace()` calls after successful login

---

## AKD-wide conventions (true of all AKD frontends)

These patterns hold across the ecosystem regardless of which specific project you're in:

**Tech stack**
- Next.js with TypeScript, App Router
- Tailwind CSS — class names are unstable, never use them as selectors
- Radix UI primitives or shadcn-style components — use `getByRole()` with these
- `lucide-react` for icons — don't assert on icon presence, assert on the surrounding interactive element

**Selector priority** (most to least stable)
1. `getByRole()` with a name or regex
2. `getByLabel()` for form fields
3. `getByText()` for readable content
4. `getByPlaceholder()` for inputs without labels
5. `locator('[data-testid