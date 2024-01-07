def ciudad_pais(ciudad, pais, poblacion=None):
	salida = f'{ciudad.title()}, {pais.title()}'
	if poblacion:
		salida += f' - {poblacion} habitantes'
	return	salida