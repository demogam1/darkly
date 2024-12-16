import requests
from bs4 import BeautifulSoup
import os
import re
# URL racine
BASE_URL = "http://172.28.248.127/.hidden/"
# Expression régulière pour vérifier si le contenu contient à la fois des lettres et des chiffres
PATTERN = re.compile(r'[A-Za-z].*\d|\d.*[A-Za-z]')
# Fonction pour explorer et filtrer les fichiers README
def fetch_readmes_with_digits(url, visited=set()):
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
                readme_content = requests.get(new_url).text.strip()
                if PATTERN.search(readme_content):  # Vérifie si le contenu contient des lettres et des chiffres
                    print(f"\n[+] Contenu trouvé avec lettres et chiffres : {new_url}")
                    print(readme_content)
            elif link.endswith("/"):  # Si c'est un sous-dossier, exploration récursive
                if new_url not in visited:
                    visited.add(new_url)
                    fetch_readmes_with_digits(new_url, visited)
    except Exception as e:
        print(f"Erreur : {e}")
if __name__ == "__main__":
    print("Recherche des fichiers README contenant des lettres et des chiffres...")
    fetch_readmes_with_digits(BASE_URL)