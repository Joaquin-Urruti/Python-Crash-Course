print('Para salir pulse "q"')

while True:
	try:
		num1 = input('Ingrese un número: ')
		if num1 == 'quit':
			break

		num2 = input('Ingrese otro número: ')
		if num2 == 'quit':
			break

	except ValueError:
		print('Solo se pueden sumar números.')

	else:
		resultado = float(num1) + float(num2)
		print(f'{num1} + {num2} = {resultado}')