# ads_links_resolver_tool — Auth

## MCP authorization (secret — reference only)

- Hosted on the `ads-ascl` MCP server, shared with `ads_search_tool` and `ascl_search_tool`; the connection uses a bearer `authorization` token from the MCP client config; `require_approval: "never"`.
- **Treat this token as a secret.** The literal value lives only in private MCP client configuration and MUST NOT be copied into this workspace. It is not reproduced here.
