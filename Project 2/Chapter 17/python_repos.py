import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

# Guardamos la respuesta
response_dict = r.json()

# Procesa los resultados
print(response_dict.keys())
print(f"Repositorios totales: {response_dict['total_count']}")

repo_dicts = response_dict["items"]
print(f"Repositorios retornados: {len(repo_dicts)}")

# Examina el primer repositorio
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)