def sumar(num1, num2):
	try:
		resultado = float(num1) + float(num2)
	except ValueError:
		print('Solo se pueden sumar valores numericos')
	else:
		print(f'{num1} + {num2} = {resultado}')

sumar(2,3)
sumar('dos', 3)