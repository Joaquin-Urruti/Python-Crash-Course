usuarios = ['Juan', 'Pedro', 'Martin', 'admin', 'Joaquin', 'Barbi', 'Santiago']

for usuario in usuarios:
	if usuario == 'admin':
		print('Hola Administrador, quiere un informe de estado?')
	else:
		print(f'Hola {usuario}, gracias por volver a entrar.')

