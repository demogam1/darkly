import requests
from bs4 import BeautifulSoup
import os

# URL racine
BASE_URL = "http://172.22.114.121/.hidden/"

# Fonction pour récupérer et afficher les contenus des fichiers README
def fetch_readmes(url, visited=set()):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erreur d'accès : {url} ({response.status_code})")
            return
        
        # Analyser le HTML pour trouver les liens
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True) if a['href'] not in ['../', '/']]
        
        for link in links:
            new_url = os.path.join(url, link)
            if link.lower() == "readme":  # Si un fichier README est trouvé
                print(f"\n[+] Contenu du fichier : {new_url}")
                readme_content = requests.get(new_url).text
                print(readme_content.strip())
            elif link.endswith("/"):  # Si c'est un sous-dossier, exploration récursive
                if new_url not in visited:
                    visited.add(new_url)
                    fetch_readmes(new_url, visited)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    print("Démarrage de l'exploration des fichiers README...")
    fetch_readmes(BASE_URL)
