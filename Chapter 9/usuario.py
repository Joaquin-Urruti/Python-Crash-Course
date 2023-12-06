class Usuario:
	"""Información del usuario
	   Parametros: nombre, npellido, edad y sexo.
	"""
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def describir_usuario(self):
		print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}\n')

	def saludar_usuario(self):
		print(f'Hola {self.nombre.title()}!\n')