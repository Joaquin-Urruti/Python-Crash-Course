ciudades = {
	'Buenos Aires': {'pais': 'Argentina', 'poblacion':16_660_000, 'curiosidad':'Tango'},
	'Montevideo': {'pais': 'Uruguay', 'poblacion':1_381_000, 'curiosidad':'Mate'},
	'New York': {'pais': 'USA', 'poblacion':8_468_000, 'curiosidad':'Jazz'},
}

for ciudad, datos in ciudades.items():
	print(f'\nCiudad:')
	for k, v in datos.items():
		if type(v) == str:
			print(f'\t{k.title()}: {v.title()}')
		else:
			print(f'\t{k.title()}: {v}')