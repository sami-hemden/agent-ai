import requests

url = "http://localhost:11434/api/generate"

donnees = {
    "model": "llama3.2",
    "prompt": "Explique l'IA en une phrase.",
    "stream": False,
}

reponse = requests.post(url, json=donnees)

print(reponse.json()["response"])