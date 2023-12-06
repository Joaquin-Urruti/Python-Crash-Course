class Restaurant:
	""" Esta clase representa un Restaurant """

	def __init__(self, nombre_restaurant, tipo_cocina):
		self.nombre_restaurant = nombre_restaurant
		self.tipo_cocina = tipo_cocina

	def describir_restaurant(self):
		print(f'Nombre del restaurant: {self.nombre_restaurant.title()}')
		print(f'Tipo de cocina: {self.tipo_cocina.title()}')

	def abrir_restaurant(self):
		print(f'El restaurant "{self.nombre_restaurant} está abierto!')