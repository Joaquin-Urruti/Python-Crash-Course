class Usuario:
	"""Información del usuario
	   Parametros: Nombre, Apellido, edad y sexo.
	"""
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def describir_usuario(self):
		print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}\n')

	def saludar_usuario(self):
		print(f'Hola {self.nombre.title()}!\n')


class Admin(Usuario):
	def __init__(self, nombre, apellido):
		super().__init__(nombre, apellido)
		self.privilegios = Privilegios()


class Privilegios():
	"""Privilegios de usuario"""
	def __init__(self, privilegios=[]):
		self.privilegios = privilegios

	def show_privileges(self):
		if self.privilegios:
			print('Ud. cuenta con los siguientes privilegios:')
			for privilegio in self.privilegios:
				print(f' - {privilegio}')
		else:
			print('Ud. no tiene privilegios de administrador')


admin = Admin('German', 'Perez')

admin.describir_usuario()

admin.privilegios.privilegios = ['puede añadir usuarios', 'puede borrar usuarios', 'puede vetar usuarios']

admin.privilegios.show_privileges()
