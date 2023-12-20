import json

def get_stored_username():
	""" Obtiene un nombre de usuario almacenado si está disponible."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
			return None
	else:
		return username


def greet_user():
	""" Saluda al usuario por su nombre."""
	username = get_stored_username()
	respuesta = input(f"Tu no nombre es {username}? ")
	
	if respuesta.lower() == 'no':
		username = input("Disculpa, cuál es tu nombre? ")
		filename = 'username.json'
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"Te recordaré para cuando vuelvas, {username}")

	elif respuesta.lower() == 'si':
		print(f'Bienvenido de nuevo, {username}')

	else:
		username = input("Cuál es tu nombre? ")
		filename = 'username.json'
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"Te recordaré para cuando vuelvas, {username}")


greet_user()