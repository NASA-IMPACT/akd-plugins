# AKD Playwright Testing Plugin

Cowork skills (and Claude Code equivalents) for setting up and writing Playwright end-to-end tests across any AKD ecosystem Next.js frontend.

## Skills

| Skill | Claude Code | Cowork | What it does |
|---|---|---|---|
| playwright-scaffold | `/akd-playwright:playwright-scaffold` | `/playwright-scaffold` | One-time setup: installs Playwright, generates config, creates `e2e/` structure |
| playwright-test-writer | `/akd-playwright:playwright-test-writer` | `/playwright-test-writer` | Generates Page Object Model + spec file for a given page or flow |

Both skills work by **reading the project's actual source files** to detect auth, routing, port, and UI element details — no hardcoded project names. Compatible with any current or future AKD Next.js frontend.

## Install (Claude Code)

```
/plugin install akd-playwright@akd-agents
```

## Install (Cowork / Claude Desktop)

Install the `.skill` files from the `cowork/` directory via **Settings → Capabilities → Skills → Install from file**:
- `cowork/playwright-scaffold.skill`
- `cowork/playwright-test-writer.skill`

## Usage

### 1. Scaffold a project (run once)

```
/playwright-scaffold
```

Reads `next.config.ts`, `package.json`, and `src/app/` to determine auth needs, export type, and port. Generates:

```
playwright.config.ts
.env.e2e.example
e2e/
  .auth/          ← gitignored
  pages/
  tests/
  fixtures.ts
  auth.setup.ts   ← auth projects only
```

After scaffolding, add the scripts to `package.json` (the skill tells you exactly what), copy `.env.e2e.example` → `.env.e2e`, and install Playwright:

```bash
npm install -D @playwright/test && npx playwright install chromium
npm run e2e        # run all tests
npm run e2e:ui     # interactive runner
```

### 2. Write tests for a page or flow

```
/playwright-test-writer
```

Describe the target: *"Write a test for the agents page"* or *"Test the login flow — success and wrong password"*. The skill reads the component source, derives selectors from the actual markup, and generates a typed POM + spec file.

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `BASE_URL` | Always | e.g. `http://localhost:3000` |
| `E2E_USERNAME` | Auth projects only | Test account email |
| `E2E_PASSWORD` | Auth projects only | Test account password |

## Project compatibility

Works on any AKD Next.js frontend. Tested on:
- **akd-labs** (Next.js + auth + FastAPI proxy)
- **akd-flow** (Next.js static export, no auth)
