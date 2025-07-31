
import asyncio


from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.models.ollama import OllamaModel
from strands.tools.mcp.mcp_client import MCPClient

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def create_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")

mcp_client = MCPClient(create_transport)


with mcp_client:

    tools = mcp_client.list_tools_sync()
    ollama_model = OllamaModel(
        host="http://localhost:11434",
        model_id="llama3.1"
    )
    agent = Agent(
        tools=tools,
        model=ollama_model
    )
    réponse = agent("Peux-tu additionner 123 et 77 pour moi ?")
    print(réponse)