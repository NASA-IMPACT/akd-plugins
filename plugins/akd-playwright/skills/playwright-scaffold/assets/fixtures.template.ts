import { test as base, expect } from '@playwright/test';

/**
 * AKD shared test fixtures.
 * Import `test` and `expect` from this file instead of '@playwright/test'
 * in your spec files. Add shared setup, custom matchers, or helper
 * page-object instantiation here as the suite grows.
 *
 * Example usage in a spec:
 *   import { test, expect } from '../fixtures';
 */

// Extend with your own fixtures as needed:
// type MyFixtures = { myHelper: MyHelperClass };
// export const test = base.extend<MyFixtures>({ ... });

export const test = base;
export { expect };
