from mcp.server import FastMCP

# 1. Instanciation du serveur MCP
mcp = FastMCP("Calculator Server")

# 2. Déclaration d'un outil : addition de deux nombres
@mcp.tool(description="Add two numbers together")
def add(x: int, y: int) -> int:
    return x + y

# 3. Lancement de l'API Streamable HTTP sur http://localhost:8000/mcp/
if __name__ == "__main__":
    mcp.run(transport="streamable-http")