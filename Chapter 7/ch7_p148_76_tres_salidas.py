prompt = '\nCuál es su edad?'
prompt += '\n(para salir escriba: quit)\n'

active = True

while active:
	edad = input(prompt)

	if edad == 'quit':
		active = False

	elif int(edad) < 3:
		print('Tu ticket es gratuito!')	
	elif int(edad) < 12:
		print('Tu ticket cuesta 8 euros')
	elif int(edad) > 12:
		print('Tu ticket cuesta 12 euros')
	elif edad == 'quit':
		break

