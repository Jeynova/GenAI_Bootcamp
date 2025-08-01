import os
import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
]

def get_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "Pas de titre"

        for selector in [
            ('div', {'class': 'main-content'}),
            ('article', {}),
            ('div', {'id': 'post-content'}),
        ]:
            element = soup.find(*selector)
            if element:
                content = element.get_text(separator="\n", strip=True)
                break
        else:
            paragraph = soup.find('p')
            content = paragraph.get_text(strip=True) if paragraph else "Pas de contenu trouvé"
        
        print(f"{url} -> {title} | {content[:40]}...")
        return {"url": url, "title": title, "content": content}
    except Exception as e:
        print(f"Erreur sur {url}: {e}")
        return {"url": url, "title": None, "content": None, "error": str(e)}
    
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(get_content, urls))
    json_path = os.path.join("data", "resultats_contenu.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nRésultats enregistrés dans : {json_path}")