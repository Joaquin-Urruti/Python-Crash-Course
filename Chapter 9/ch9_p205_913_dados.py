import random as r

class Dado():
	"""Clase que representa un dado de varias caras"""
	def __init__(self, caras=6):
		self.caras = caras

	def tirar_dado(self):
		self.cara = r.randrange(1, self.caras)
		print(f'Cara del tiro: {self.cara}')

dado_6 = Dado()
dado_10 = Dado(10)
dado_20 = Dado(20)

print('\nDado de 6 caras')
for i in range(10):
	dado_6.tirar_dado()

print('\nDado de 10 caras')
for i in range(1, 10):
	dado_10.tirar_dado()

print('\nDado de 20 caras')
for i in range(10):
	dado_20.tirar_dado()