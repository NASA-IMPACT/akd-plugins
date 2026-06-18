import { test as setup, expect } from '@playwright/test';
import path from 'path';

/**
 * AKD auth setup — logs in once and saves session state.
 * Playwright runs this before any test in a project that declares
 * `dependencies: ['setup']`. All subsequent tests reuse the saved
 * cookies / localStorage rather than logging in again.
 *
 * Requires env vars:
 *   E2E_USERNAME — login email
 *   E2E_PASSWORD — login password
 */

const AUTH_FILE = path.join(__dirname, '.auth/user.json');

setup('authenticate', async ({ page }) => {
  const username = process.env.E2E_USERNAME;
  const password = process.env.E2E_PASSWORD;

  if (!username || !password) {
    throw new Error(
      'E2E_USERNAME and E2E_PASSWORD must be set. ' +
      'Copy .env.e2e.example to .env.e2e and fill in your credentials.'
    );
  }

  await page.goto('/login');

  // Fill the login form — adjust selectors if the form changes
  await page.getByLabel(/email/i).fill(username);
  await page.getByLabel(/password/i).fill(password);
  await page.getByRole('button', { name: /sign in|log in|login/i }).click();

  // Wait until we've landed on a post-login page
  await expect(page).not.toHaveURL(/\/login/);

  // Save auth state for reuse across all tests
  await page.context().storageState({ path: AUTH_FILE });
});
