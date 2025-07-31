import json
import os

# Dossier de données
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
FILENAME = os.path.join(DATA_DIR, 'state.json')

# Charge l'état depuis un fichier JSON (ou initialise vide)
def load_state():
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Sauvegarde l'état complet dans le fichier JSON
def save_state(state):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(FILENAME, 'w') as f:
        json.dump(state, f, indent=2)