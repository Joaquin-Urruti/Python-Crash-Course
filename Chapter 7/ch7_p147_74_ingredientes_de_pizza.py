prompt = 'Escriba los ingredientes que quiere agregar a su pizza:'
prompt += '\n(Cuando termine escriba "quit")'

while True:
	ingredientes = input(prompt)

	if ingredientes != 'quit':
		print(f'Agregaremos {ingredientes} a su pizza')
	elif ingredientes == 'quit':
		break
