---
name: playwright-test-writer
description: Writes Playwright e2e test specs and Page Object Models for any AKD ecosystem Next.js project. Use this skill whenever someone wants to write, generate, or add browser tests for a specific page, feature, or user flow in any AKD frontend. Triggers on phrases like "write a test for", "add e2e coverage for", "test the login flow", "generate a spec for this page", or when reviewing a component and wanting to test it end-to-end. Assumes playwright-scaffold has already been run (playwright.config.ts and e2e/ folder exist). If they don't, run playwright-scaffold first.
---

# Playwright Test Writer

This skill generates Playwright test specs and Page Object Models (POMs) for AKD frontends. It works by reading the relevant source files to understand the actual UI — selectors are derived from the code, not guessed.

## Before writing anything

Read `references/akd-project-patterns.md` for the project's selector conventions, API proxy setup, and folder structure.

Confirm that `playwright.config.ts` and `e2e/` exist in the project root. If they don't, tell the user to run `/playwright-scaffold` first.

## Step 1: Understand what to test

Identify the target from the user's request — it might be:
- A route/page (e.g. "test the agents page")
- A user flow (e.g. "test that I can create a new benchmark run")
- A component behavior (e.g. "test that the file upload shows an error on bad file type")

If ambiguous, ask one clarifying question: "Which page or flow do you want covered?"

## Step 2: Read the source — derive selectors, don't invent them

Read the relevant files before writing a single locator:
- `src/app/[route]/page.tsx` — the page component
- `src/app/[route]/layout.tsx` — if there's a section-level layout
- Key child components the feature relies on (use judgment — focus on what's relevant to the tested behavior)

From the source, extract:

**Entry points** — the URL to navigate to (respect `trailingSlash: true` if set in `next.config.ts`)

**Interactive elements** — for each form, button, modal, or table:
- What is the element type? (`<button>`, `<a>`, `<input>`, `<dialog>`)
- What label, aria-label, placeholder, or visible text identifies it?
- Use that to write the selector — e.g. if the label is literally `"Email address"`, use `getByLabel('Email address')`, not `getByLabel(/email/i)`

**Success and error states** — find the exact element that renders after an action:
- For success: what appears, what URL changes to, what disappears
- For errors: find the actual error element in the component code. Look for conditional renders like `{error && <p>...</p>}`, toast calls, or ARIA roles. **Read the actual markup — do not assume `getByRole('alert')` will work.** If the error is a plain `<p>` or `<div>`, use `getByText(/pattern/)` or the most stable attribute you can find.

**API calls** — any `fetch`/`useQuery`/`useMutation` calls tell you which endpoints are involved and what shapes to mock if needed.

## Step 3: Write the Page Object Model

Create `e2e/pages/[feature].page.ts` with a class that encapsulates locators and action methods. Keep it thin — locators and one-liner actions belong here; assertions stay in the spec.

```typescript
// e2e/pages/agents.page.ts
import { Page, Locator } from '@playwright/test';

export class AgentsPage {
  readonly page: Page;
  readonly newAgentButton: Locator;
  readonly agentCards: Locator;

  constructor(page: Page) {
    this.page = page;
    // Use exact text/role from the source — not guesses
    this.newAgentButton = page.getByRole('link', { name: /new agent/i });
    this.agentCards = page.getByRole('article');
  }

  async goto() {
    await this.page.goto('/agents');
  }

  async clickNewAgent() {
    await this.newAgentButton.click();
  }
}
```

**Selector priority** (most to least stable for AKD UIs):
1. `getByRole()` with the exact visible name or a regex
2. `getByLabel()` for form fields — use the exact label text when you can read it
3. `getByText()` for readable content
4. `getByPlaceholder()` for inputs without labels
5. `locator('[data-testid=...]')` — only if test IDs are already in the codebase
6. CSS class selectors — **never** (Tailwind classes change constantly)

When a locator can't be derived confidently from the source, leave an explicit comment: `// ⚠️ verify this selector against live markup`

## Step 4: Write the spec file

Create `e2e/tests/[feature].spec.ts`. Import from `../fixtures` — not directly from `@playwright/test` — so the shared fixture type is used across all AKD tests.

```typescript
import { test, expect } from '../fixtures';
import { AgentsPage } from '../pages/agents.page';

test.describe('Agents page', () => {
  let agentsPage: AgentsPage;

  test.beforeEach(async ({ page }) => {
    agentsPage = new AgentsPage(page);
    await agentsPage.goto();
  });

  test('shows the agents list', async ({ page }) => {
    await expect(agentsPage.agentCards).not.toHaveCount(0);
  });

  test('navigates to new agent form', async ({ page }) => {
    await agentsPage.clickNewAgent();
    await expect(page).toHaveURL(/\/agents\/new/);
  });
});
```

**Test naming**: `'[subject] [verb] [outcome]'` — reads like a sentence, no "should" prefix.

**Good patterns for AKD:**
- Forms: fill → submit → assert on success/error UI state (using selectors derived from the actual error element)
- Lists/tables: assert count > 0, assert specific content is visible
- Modals/dialogs: open → interact → assert dialog gone + effect applied
- Navigation: click → assert URL changed AND meaningful content loaded

## Step 5: Handle API-dependent tests

AKD backends are FastAPI services. Tests hit the real API by default — this is intentional for integration confidence.

Use `page.route()` when testing error states or avoiding side effects:

```typescript
test('shows error when API is down', async ({ page }) => {
  await page.route('/api/agents', route => route.fulfill({
    stat