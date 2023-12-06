from usuario import Usuario

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


