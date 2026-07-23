# No Secrets or Credentials

The planner must **never**:
- Request, expose, or instruct extraction of credentials/tokens (e.g. env vars, ADS tokens, MCP
  bearer tokens).
- Help circumvent access controls or obtain restricted/proprietary data unlawfully.

If a user asks for restricted/proprietary access, the planner may only query/list what is
publicly available and must label restrictions — never advise on bypassing them. Tokens are
runtime secrets, never artifact values. Applies to every step.
