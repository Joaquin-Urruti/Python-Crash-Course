class Usuario:
	"""Información del usuario
	   Parametros: Nombre, Apellido, edad y sexo.
	"""
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def describir_usuario(self):
		print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}, Edad: {self.edad}, Sexo: {self.sexo.title()}\n')

	def saludar_usuario(self):
		print(f'Hola {self.nombre.title()}!\n')


class Admin(Usuario):
	def __init__(self, nombre, apellido):
		super().__init__(nombre, apellido)
		self.privilegios = ['puede añadir usuarios', 'puede borrar usuarios', 'puede vetar usuarios']

	def show_privileges(self):
		print('Como administrador ud. cuenta con los siguientes privilegios:')
		for privilegios in self.privilegios:
			print(f'{privilegios}')

admin = Admin('Pepe', 'Gonzalez')

admin.show_privileges()