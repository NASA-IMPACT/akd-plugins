---
name: playwright-scaffold
description: Sets up Playwright e2e testing infrastructure for any AKD ecosystem Next.js project. Use this skill whenever someone wants to add e2e tests, set up Playwright, scaffold a testing folder, or wire up browser-based tests in any AKD project — including new or unfamiliar ones. Triggers on phrases like "set up Playwright", "add e2e tests", "scaffold testing", "I want to write browser tests", or when someone is working in an akd-* frontend repo and mentions testing.
---

# Playwright Scaffold

This skill installs and configures Playwright for any AKD ecosystem Next.js frontend. It works by reading the project's actual files to determine what's needed — it does not rely on recognizing the project by name.

## Step 1: Read the project

Before making any decisions, read these files in order:

1. **`next.config.ts`** (or `next.config.js`) — extract: `output: 'export'` (static?), `rewrites()` (API proxy destination and port?), `trailingSlash`, custom port
2. **`package.json`** — extract: existing scripts (what port does `dev` run on?), whether `@playwright/test` is already installed
3. **`src/app/` directory listing** — look for a `login/`, `signin/`, or `auth/` route directory
4. **Login page component** (if a login route exists) — read `src/app/[login-route]/page.tsx` to find: the exact email input label, password input label, submit button text, error element markup, and post-login redirect target

Derive everything from what you read. Consult `references/akd-project-patterns.md` for the detection decision tree and AKD-wide conventions.

From your reads, determine:
- **Auth required?** A login route directory exists → yes. No login route → no.
- **Static export?** `output: 'export'` present → yes.
- **API proxy?** `rewrites()` present → note destination host/port for documentation.
- **Default port?** Check the `dev` script in `package.json` for an explicit port; otherwise default to 3000.
- **Existing Playwright?** `@playwright/test` in `devDependencies` or `playwright.config.ts` already exists → don't reinstall; scaffold only what's missing.

## Step 2: Install Playwright

If `@playwright/test` is not already in `devDependencies`, add it:

```bash
npm install -D @playwright/test
npx playwright install chromium
```

If the user is in a CI-only context or wants all browsers:
```bash
npx playwright install --with-deps
```

## Step 3: Generate `playwright.config.ts`

Use the appropriate template from `assets/`:

- **With auth** → `playwright.config.auth.template.ts`
- **Without auth** → `playwright.config.noauth.template.ts`

Write the file to the project root as `playwright.config.ts`. Substitute:
- `BASE_URL` placeholder → keep as `process.env.BASE_URL ?? 'http://localhost:3000'` (correct for most AKD projects; adjust port if the project uses a different default)
- `STORAGE_STATE_PATH` → `'e2e/.auth/user.json'`

## Step 4: Create the `e2e/` folder structure

Create these files and directories:

```
e2e/
  .auth/               ← gitignored; Playwright writes auth state here
  pages/               ← Page Object Models go here (one file per major route)
  tests/               ← Spec files go here
  fixtures.ts          ← Extended test object with shared setup
```

Write `e2e/fixtures.ts` from `assets/fixtures.template.ts`.

If auth is required, also write `e2e/auth.setup.ts` from `assets/auth.setup.template.ts`. Substitute:
- The login URL (e.g. `/login`, `/signin`) — from what you read in Step 1
- The email selector — use the exact label text you found in the login component (e.g. `getByLabel('Email')` not `getByLabel(/email/i)` if the label is exact)
- The password selector — same approach
- The submit button name — use the exact button copy found in the component
- The post-login URL pattern — from the redirect call in the login component

Add `e2e/.auth/` to `.gitignore` if not already present (auth state contains live session cookies — never commit it).

## Step 5: Update `package.json`

Add these scripts under `"scripts"`:

```json
"e2e":         "playwright test",
"e2e:ui":      "playwright test --ui",
"e2e:headed":  "playwright test --headed",
"e2e:codegen": "playwright codegen ${BASE_URL:-http://localhost:3000}"
```

Do not overwrite existing scripts — merge them in.

## Step 6: Create `.env.e2e.example`

Write this file to the project root:

```
# Copy to .env.e2e and fill in values before running e2e tests locally.
# In CI, inject these as environment variables.

BASE_URL=http://localhost:3000

# Only needed for projects with authentication:
E2E_USERNAME=your@email.com
E2E_PASSWORD=yourpassword
```

Add `.env.e2e` (but NOT `.env.e2e.example`) to `.gitignore`.

## Step 7: Confirm and summarize

Tell the user what was created, what commands to run next, and what they'll need to fill in (env vars, login selectors if auth was scaffolded). Keep it brief — one short paragraph and a command block.

Example closing:
> Playwright is set up. Run `npm run e2e` to execute tests (make sure the dev server