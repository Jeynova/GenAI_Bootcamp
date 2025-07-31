import requests
from state_store import load_state, save_state

HIGH_THRESHOLD = 7
MEDIUM_THRESHOLD = 4

def register_tools(mcp):
    # Charge l’état (crée data/ s’il n’existe pas)
    state = load_state()

    @mcp.tool(description="Évaluer la sévérité des symptômes (stub)")
    def symptom_checker(symptoms: str) -> dict:
        # Remplacez ici par un vrai appel ou un rule-based
        score = min(10, max(1, sum(len(w) for w in symptoms.split()) // 5))
        return {"urgency_score": score, "details": f"score simulé {score}/10"}

    @mcp.tool(description="Dispatcher une ambulance à l'adresse donnée")
    def dispatch_ambulance(location: str, caller_id: str = None) -> str:
        return f"Ambulance envoyée à {location}"

    @mcp.tool(description="Donner le centre d’urgent care le plus proche")
    def urgent_care(location: str) -> str:
        return f"Centre d’urgent care à proximité de {location}"

    @mcp.tool(description="Fournir des instructions d'auto-soin")
    def self_care(symptoms: str) -> str:
        return f"Conseils d’auto-soin pour : {symptoms}"

    @mcp.tool(description="Enregistrer l’état d’un appel")
    def persist_state(tool_use_id: str, symptoms: str, score: int, action: str) -> str:
        # Stocke l'état dans data/state.json
        state[tool_use_id] = {
            "symptoms": symptoms,
            "score": score,
            "action": action
        }
        save_state(state)
        return "OK"