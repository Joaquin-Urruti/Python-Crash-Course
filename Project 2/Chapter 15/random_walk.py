from random import choice

class RandomWalk():
	"""Clase para generar caminos aleatorios"""
	def __init__(self, num_points=5_000):
		"""Inicializa los atributos de una camino"""
		self.num_points = num_points

		'Todos los caminos empiezan en 0, 0.'
		self.x_values = [0]
		self.y_values = [0]


	def fill_walk(self):
		"""Calcula todos los puntos del camino"""

		# Sigue dando pasos hasta que el camino tiene la longitud elegida
		while len(self.x_values) < self.num_points:

			# Decide en qué dirección ir
			x_step = self.get_step()
			y_step = self.get_step()

			# Rechaza los movimientos que no van a ninguna parte
			if x_step == 0 and y_step == 0:
				continue

			# Calcula la posición
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

	def get_step(self, direction_vals=[-1, 1], distance_vals=[0, 1, 2, 3, 4, 5, 6, 7, 8]):
		"Calcula la distancia y la dirección de un paso"
		direction = choice(direction_vals)
		distance = choice(distance_vals)
		step = direction * distance

		return step
