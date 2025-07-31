import requests
from state_store import load_state, save_state  # import de la persistance

HIGH_THRESHOLD = 7
MEDIUM_THRESHOLD = 4

def register_tools(mcp):
    # Charge l’état ou initialise vide
    state = load_state()

    @mcp.tool(description="Évaluer la sévérité des symptômes via un API externe")
    def symptom_checker(symptoms: str) -> dict:
        return {"urgency_score": 8, "details": "douleur thoracique 8/10"}

    @mcp.tool(description="Dispatcher une ambulance à l'adresse donnée")
    def dispatch_ambulance(location: str, caller_id: str = None) -> str:
        return f"Ambulance envoyée à {location}"

    @mcp.tool(description="Donner le centre d’urgent care le plus proche")
    def urgent_care(location: str) -> str:
        return f"Centre d’urgent care à proximité de {location}"

    @mcp.tool(description="Fournir des instructions d'auto-soin")
    def self_care(symptoms: str) -> str:
        return f"Conseils d’auto-soin pour : {symptoms}"

    @mcp.tool(description="Orchestre le triage et dispatch selon la sévérité")
    def triage_call(symptoms: str, location: str, caller_id: str = None, tool_use_id: str = None) -> str:
        # 1. Récupération du score
        result = symptom_checker(symptoms)
        score = result["urgency_score"]

        # 2. Décision
        if score >= HIGH_THRESHOLD:
            action = dispatch_ambulance(location, caller_id)
        elif score >= MEDIUM_THRESHOLD:
            action = urgent_care(location)
        else:
            action = self_care(symptoms)

        # 3. Mise à jour de l'état
        if tool_use_id:
            state[tool_use_id] = {
                "symptoms": symptoms,
                "score": score,
                "action": action
            }
            save_state(state)

        return action