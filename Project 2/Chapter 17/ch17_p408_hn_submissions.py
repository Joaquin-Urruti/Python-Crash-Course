from operator import itemgetter
import requests

# Hace una llamada a la API y guarda la respuesta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

