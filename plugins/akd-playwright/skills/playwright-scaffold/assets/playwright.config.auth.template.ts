import { defineConfig, devices } from '@playwright/test';

/**
 * AKD Playwright config — authenticated project variant.
 * Env vars (set in .env.e2e locally, injected in CI):
 *   BASE_URL      — e.g. http://localhost:3000
 *   E2E_USERNAME  — login email
 *   E2E_PASSWORD  — login password
 */
export default defineConfig({
  testDir: './e2e/tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [['html'], ['list']],

  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    storageState: 'e2e/.auth/user.json',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },

  projects: [
    // Auth setup runs first — logs in and saves session to e2e/.auth/user.json
    {
      name: 'setup',
      testMatch: /auth\.setup\.ts/,
    },

    // All other tests depend on setup being complete
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
      dependencies: ['setup'],
    },
  ],

  // Start the dev server automatically if not already running
  webServer: {
    command: 'npm run dev',
    url: process.env.BASE_URL ?? 'http://localhost:3000',
    reuseExistingServer: true,
    timeout: 120 * 1000,
  },
});
