# Nexus MCP v0.2.0 Release Notes

## Highlights

Nexus MCP v0.2.0 expands package discovery beyond exact package names and adds
flexible HTTP transport support for local and container deployments.

- **Keyword package discovery:** Search Python packages and Docker images with
  descriptive keywords while receiving compact, model-friendly results.
- **More Nexus formats:** The new `search_other_packages` tool covers npm,
  NuGet, Raw, RubyGems, Helm, Go, Maven, and other Nexus formats. Searches can
  target a specific format or span all formats outside PyPI and Docker.
- **Streamable HTTP support:** Run the server with SSE or Streamable HTTP and
  select the host, port, and transport through CLI options or environment
  variables.
- **Published container image:** Pull the current image from
  `ghcr.io/brtydse100/sonatype-nexus-mcp:latest`.

## Package Discovery

### Keyword Search

- Added `search_python_packages` for descriptive Python package searches.
- Added `search_docker_images` for descriptive Docker image searches.
- Added `search_other_packages` for package ecosystems without a dedicated
  tool.
- Added Nexus `q` query support to the client and carried it through paginated
  searches.
- Limited keyword search output to package name, version, and repository. The
  general package search also includes the Nexus format.
- Added `max_results`, defaulting to 20, to keep responses compact.
- Reject blank keyword searches before sending a Nexus request.

### Other Package Formats

`search_other_packages` accepts an optional Nexus `format` filter. When the
filter is omitted, the search spans available formats and excludes PyPI and
Docker results because those ecosystems have dedicated tools.

Examples of supported format values include `npm`, `nuget`, `raw`, `rubygems`,
`helm`, `go`, and `maven2`.

## Transport and Serving

- Added `--transport`, `--host`, and `--port` command-line options.
- Added matching `NEXUS_MCP_TRANSPORT`, `NEXUS_MCP_HOST`, and
  `NEXUS_MCP_PORT` environment variables.
- Command-line values take precedence over environment values.
- Added Streamable HTTP alongside the existing SSE transport.
- Streamable HTTP is now the default transport in Docker and is served at
  `/mcp`.
- Removed unsupported path arguments from the FastMCP startup call.

## Response Size Improvements

- Reduced the default Maven and Python version page size from 50 to 20.
- Capped keyword searches at 20 results by default.
- Preserved continuation tokens for clients that need additional version
  pages.

## Container Distribution

- Added a GitHub Actions workflow that builds and publishes the project image
  to GitHub Container Registry.
- Updated Docker Compose, build scripts, and documentation to use
  `ghcr.io/brtydse100/sonatype-nexus-mcp`.
- Added commit-specific image tags alongside `latest` on the default branch.

## Compatibility

- Python 3.10 or newer is required.
- The server remains read-only and uses the Nexus REST API v1.
- Existing Maven, PyPI, and Docker tools remain available.

## Installation

Install the Python package:

```bash
pip install nexus-mcp-server==0.2.0
```

Or run the container:

```bash
docker run -p 8000:8000 ghcr.io/brtydse100/sonatype-nexus-mcp:latest
```
