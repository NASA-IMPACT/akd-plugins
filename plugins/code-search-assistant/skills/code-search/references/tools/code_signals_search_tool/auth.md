# code_signals_search_tool — Auth

## MCP authorization (secret — reference only)

- Hosted on the `Code_Signal` MCP server; the connection uses a bearer `authorization` token from the MCP client config; `require_approval: "never"`.
- **Treat this token as a secret.** The literal value lives only in private MCP client configuration and MUST NOT be copied into this workspace. It is not reproduced here.
