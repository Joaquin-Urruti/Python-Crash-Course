respuestas = {}

polling_active = True

while polling_active:
	nombre = input('\nCuál es su nombre? ')
	respuesta = input('\nSi pudieras visitar cualquier lugar del mundo, adónde irías? ')

	respuestas[nombre] = respuesta

	repregunta = input('\nQuieres que alguien más responda la encuesta? (si/no): ')

	if repregunta == 'no':
		polling_active = False

print('\n --- Resultados de la Encuesta ---')
for nombre, respuesta in respuestas.items():
	print(f'A {nombre} le gustaría ir a {respuesta}')