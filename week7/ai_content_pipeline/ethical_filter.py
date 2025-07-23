import re

# Listes extensibles de mots-clés sensibles
HATE_KEYWORDS = ["kill", "hate", "nazi", "racist", "rape", "terrorist"]
SLUR_KEYWORDS = ["retard", "idiot", "bastard"]
VIOLENCE_KEYWORDS = ["murder", "gun", "explode", "blood", "death"]
ABSURDITY_KEYWORDS = ["unicorns", "brainwash", "zombies", "aliens"]

ALL_KEYWORDS = HATE_KEYWORDS + SLUR_KEYWORDS + VIOLENCE_KEYWORDS + ABSURDITY_KEYWORDS


def ethical_filter(text: str) -> dict:
    """
    Analyse un texte pour détecter des dérives éthiques simples.

    Args:
        text (str): texte à analyser

    Returns:
        dict: informations sur les mots trouvés et statut
    """
    found = [kw for kw in ALL_KEYWORDS if re.search(rf"\b{kw}\b", text.lower())]
    flagged = len(found) > 0
    return {
        "flagged": flagged,
        "keywords": found,
        "status": "Dérive détectée" if flagged else "OK"
    }