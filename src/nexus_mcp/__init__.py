"""Nexus MCP Server - Query Sonatype Nexus Repository Manager via MCP."""

__version__ = "0.2.0"


def main() -> None:
    """Entry point for the nexus-mcp command."""
    from nexus_mcp.server import run_server

    run_server()
