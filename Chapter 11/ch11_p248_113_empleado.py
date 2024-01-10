class Empleado:
	"""Clase que representa a un empleado"""

	def __init__(self, nombre, apellido, salario_anual):
		"""Guarda los datos del empleado"""
		self.nombre =  nombre
		self.apellido = apellido
		self.salario_anual = salario_anual

	def detalle(self):
		"""Muestra los datos del empleado"""
		print(f'{self.nombre.title()} {self.apellido.title()} gana {self.salario_anual} al año.')

	def dar_aumento(self, aumento=5_000):
		self.salario_anual = self.salario_anual + aumento
		print(f'El nuevo sueldo de {self.nombre.title()} es de: {self.salario_anual} al año.')