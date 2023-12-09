prompt = 'Escriba "quit" para salir\n'
prompt += 'Por qué te gusta programar? '

while True:
	respuesta = input(prompt)
	if respuesta == 'quit':
		break

	with open('encuesta_programacion.txt', 'a') as file:
		file.write(f'{respuesta}\n')