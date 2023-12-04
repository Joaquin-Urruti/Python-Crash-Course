rios = {
	'Paraná': 'Argentina',
	'Nilo': 'Egipto',
	'Amazonas': 'Brasil',
}

for rio, pais in rios.items():
	print(f'El {rio.title()} discurre por {pais.title()}')

print('\nRíos:')

for rio in rios.keys():
	print(rio.title())

print('\nPaises:')

for pais in rios.values():
	print(pais.title())