from random import randint

class Die:
	"""Clase que representa un dado"""
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def show_sides(self):
		print(f'Este dado tiene {self.num_sides} caras.')

	def roll(self):
		"""Devuelve un numero aleatorio entre 1 y el numero de caras"""
		return randint(1, self.num_sides)