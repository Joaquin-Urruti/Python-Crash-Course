lugares_favoritos = {
	'Juan': ['Suarez', 'Azul', 'Su casa'],
	'Joaquin': ['Su casa', 'Su jardin', 'el escenario'],
	'Tati': ['La parrilla', 'La cancha de tennis'],
}

for nombre, lugares in lugares_favoritos.items():
	print(f'Los lugares favoritos de {nombre} son:')
	for lugar in lugares:
		print(f'\t{lugar}')