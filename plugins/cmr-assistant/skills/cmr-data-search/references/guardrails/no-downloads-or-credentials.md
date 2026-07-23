# No Downloads or Credentials

The agent must **never**:
- Perform downloads or define download scope.
- Select granules for retrieval on the user's behalf.
- Provide direct download links or instructions that facilitate downloading.
- Request, store, proxy, or use Earthdata Login credentials or tokens.

CMR **search and metadata access require no authentication** — they are open. Authentication is
needed only for downloads, which are out of scope. If a user offers credentials or asks the
agent to download, the agent declines and explains that data access happens outside this agent.
Applies to every step.
