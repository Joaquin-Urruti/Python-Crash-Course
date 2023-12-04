class Usuario:
	"""Información del usuario
	   Parametros: Nombre, Apellido, edad y sexo.
	"""
	def __init__(self, nombre, apellido, edad, sexo):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.sexo = sexo

	def describir_usuario(self):
		print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}, Edad: {self.edad}, Sexo: {self.sexo.title()}\n')

	def saludar_usuario(self):
		print(f'Hola {self.nombre.title()}!\n')

juan = Usuario('juan', 'gonella', 42, 'masculino')
joaquin = Usuario('joaquin', 'meier', 30, 'masculino')
tordo = Usuario('tordo', 'loos', 38, 'masculino')

juan.describir_usuario()
juan.saludar_usuario()
joaquin.describir_usuario()
joaquin.saludar_usuario()
tordo.describir_usuario()
tordo.saludar_usuario()