import asyncio
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient
from strands import Agent
from strands.models.ollama import OllamaModel

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def create_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")

def main():
    mcp_client = MCPClient(create_transport)
    with mcp_client:
        # 1) Récupère la liste des tools exposés
        tools = mcp_client.list_tools_sync()
        print("Tools disponibles:", [t.tool_name for t in tools])

        # 2) Configure le modèle Ollama
        model = OllamaModel(
            host="http://localhost:11434",
            model_id="llama3.1"
        )

        # 3) Instancie l’Agent Strands
        agent = Agent(tools=tools, model=model)

        # 4) Exécution d’un scénario
        user_query = (
            "Appelle le triage pour ces symptômes : "
            "« douleur thoracique et essoufflement », "
            "adresse « 123 Rue de la Paix, Paris »."
        )
        réponse = agent(user_query)

        print("Réponse de l’agent :", réponse)

        # 5) (Optionnel) si l’agent a identifié un tool_use_id et un état,
        #    on peut appeler persist_state pour sauvegarder
        #    — Strands Agent peut renvoyer un JSON décrivant l’action et le tool_use_id.
        #    Par exemple :
        # state_info = extract_state_info(réponse)
        # mcp_client.call_tool_sync(
        #     tool_use_id="persist-0001",
        #     name="persist_state",
        #     arguments=state_info
        # )

if __name__ == "__main__":
    main()