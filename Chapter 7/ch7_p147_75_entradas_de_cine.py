prompt = '\nCuál es su edad?'
prompt += '\n(para salir escriba: quit)\n'

while True:
	edad = input(prompt)

	if edad != 'quit':
		if int(edad) < 3:
			print('Tu ticket es gratuito!')
		elif int(edad) < 12:
			print('Tu ticket cuesta 8 euros')
		else:
			print('Tu ticket cuesta 12 euros')
	else:
		break