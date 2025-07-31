from strands.tools.mcp.mcp_client import MCPClient
from mcp_client import TransportConfig

# Configure transport to local FastAPI
transport = TransportConfig(url="http://127.0.0.1:8000/mcp")
client = MCPClient(transport)

with client:
    # List tools
    print(client.list_tools_sync())
    # Call triage
    resp = client.call_tool_sync(
        tool_use_id="call123",
        name="triage_call",
        arguments={
            "transcript":"mild headache, nausea",
            "caller_info":{"name":"Martin","contact":"+33987654321"},
            "location":{"address":"20 av. de l’Opéra, Paris"}
        }
    )
    print(resp)