from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

def create_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")

mcp_client = MCPClient(create_transport)

with mcp_client:
    tools = mcp_client.list_tools_sync()
    # Liste des noms de tools
    tool_names = [t.tool_name for t in tools]
    print("Outils disponibles :", tool_names)

    # Exemple d'appel du tool "add"
    resp = mcp_client.call_tool_sync(
        tool_use_id="appel-unique-1",
        name="add",  # ou tool_names[0] si c'est le seul
        arguments={"x": 42, "y": 58}
    )
    print("42 + 58 =", resp["content"][0]["text"])