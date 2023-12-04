class Usuario:
	"""Información del usuario
	   Parametros: Nombre, Apellido, edad y sexo.
	"""
	def __init__(self, nombre, apellido, **kwargs):
		self.nombre = nombre
		self.apellido = apellido
		self.kwargs = kwargs
		self.intentos_inicio = 0

	def describir_usuario(self):
		if self.kwargs:
			print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}, Informacion: {str(self.kwargs)[1:-1]}\n')
		else:
			print(f'Nombre: {self.nombre.title()}, Apellido: {self.apellido.title()}.\n')

	def saludar_usuario(self):
		print(f'Hola {self.nombre.title()}!\n')

	def incrementar_intentos_inicio(self, incremento):
		self.intentos_inicio += 1

	def restablecer_intentos_inicio(self):
		self.intentos_inicio = 0


# pepe = Usuario(nombre='Pepe', apellido='Gonzalez')

# pepe.incrementar_intentos_inicio(1)
# pepe.incrementar_intentos_inicio(1)
# pepe.incrementar_intentos_inicio(1)
# pepe.incrementar_intentos_inicio(1)
# pepe.incrementar_intentos_inicio(1)
# pepe.incrementar_intentos_inicio(1)

# pepe.restablecer_intentos_inicio()

# print(pepe.intentos_inicio)

