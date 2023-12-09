user_prompt = 'Escriba "quit"para salir\n'
user_prompt += 'Por favor escriba su nombre: '

while True:
	name = input(user_prompt)
	if name == 'quit':
		break

	print('Bienvenido {name}! Será agregado a la lista de invitados.')
	with open('libro_invitados.txt', 'a') as file:
		file.write(f'\n{name.title()}')