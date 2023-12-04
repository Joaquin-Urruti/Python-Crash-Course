def build_profile(nombre, apellido, **user_info):
	"""Crea un diccionario con la información del usuario """
	user_info['nombre'] = nombre
	user_info['apellido'] = apellido
	return user_info