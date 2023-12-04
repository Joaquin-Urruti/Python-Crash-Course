class Restaurant:
	""" Esta clase representa un Restaurant """
	def __init__(self, nombre_restaurant, tipo_cocina):
		self.nombre_restaurant = nombre_restaurant
		self.tipo_cocina = tipo_cocina
		self.numero_servido = 0

	def describir_restaurant(self):
		print(f'Nombre del restaurant: {self.nombre_restaurant.title()}')
		print(f'Tipo de cocina: {self.tipo_cocina.title()}')

	def abrir_restaurant(self):
		print(f'El restaurant "{self.nombre_restaurant} está abierto!')

	def establecer_numero_servido(self, numero_de_clientes_servidos):
		self.numero_servido = numero_de_clientes_servidos

	def incrementar_numero_servido(self, incremento_numero_servido):
		self.numero_servido += incremento_numero_servido


class CarritoDeHelados(Restaurant):
	"""Crea un carrito de helados a partir de la clase Restaurant"""
	def __init__(self, nombre_restaurant, tipo_cocina):
		super().__init__(nombre_restaurant, tipo_cocina)
		self.sabores = ['Dulce de leche', 'Frutilla', 'Tramontana', 'Chocolate', 'Banana Split']

carrito = CarritoDeHelados(nombre_restaurant='Helados Joaquín', tipo_cocina='Heladería')

print(carrito.sabores)
