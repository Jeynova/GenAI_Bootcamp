from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

def create_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")

def main():
    mcp_client = MCPClient(create_transport)
    with mcp_client:
        # 1) lister les tools
        tools = mcp_client.list_tools_sync()
        print("Outils disponibles :", [t.tool_name for t in tools])

        # 2) appeler le triage
        resp = mcp_client.call_tool_sync(
            tool_use_id="triage-0001",
            name="triage_call",
            arguments={
                "session_id":     "triage-session-001",
                "symptoms":       "douleur thoracique et essoufflement",
                "location":       "123 Rue de la Paix, Paris",
                "caller_id":      "appelant_42",
                "tool_use_id":    "triage-0001"
            }
        )
        # resp["content"] est une liste de {"text": ...}
        print("Réponse triage_call :", resp["content"][0]["text"])

if __name__ == "__main__":
    main()