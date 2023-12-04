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


lo_de_joaco = Restaurant('lo de joaco', 'parrilla')
barbies = Restaurant("Barbie's", 'heladería')
lalus = Restaurant("Lalu's", 'pizzería')

lo_de_joaco.describir_restaurant()
barbies.describir_restaurant()
lalus.describir_restaurant()