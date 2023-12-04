def ciudad_pais(ciudad, pais):
	return f'{ciudad.title()}, {pais.title()}'

bsas = ciudad_pais('Buenos Aires', 'Argentina')
print(bsas)

bch = ciudad_pais('Bariloche', 'Argentina')
print(bch)

mv = ciudad_pais('Montevideo', 'Uruguay')
print(mv)