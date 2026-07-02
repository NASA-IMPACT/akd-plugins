# ads_search_tool — Auth

## MCP authorization (secret — reference only)

- Hosted on `ads-ascl`; bearer `authorization` token shared with `ads_links_resolver_tool` and `ascl_search_tool`.
- Uses `require_approval: "never"`.
- **Treat this token as a secret.** The literal value lives only in private MCP client configuration and MUST NOT be copied into this workspace. It is not reproduced here.
