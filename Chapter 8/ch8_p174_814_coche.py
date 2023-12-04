def make_car(marca, modelo, **auto_details):
	"""
	Crea un auto a partir del nombre y modelo.
	Toma otros detalles como parametros opcionales.
	"""
	auto_details['marca'] = marca
	auto_details['modelo'] = modelo
	return auto_details

auto = make_car('volkswagen','fox', levantavidrios=False, cierre_centralizado=False)

print(auto)