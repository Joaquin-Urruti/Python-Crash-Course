import unittest
from ciudad_funciones import ciudad_pais

class CiudadTestCase(unittest.TestCase):
	"""Pruebas para la funcion ciudad_pais"""
	def test_ciudad_pais(self):
		"""Probar si funciona el formateador"""
		salida = ciudad_pais('buenos aires', 'argentina')
		self.assertEqual(salida, 'Buenos Aires, Argentina')

	def test_ciudad_pais_habitantes(self):
		"""Probar si funciona con ciudad pais habitantes"""
		salida = ciudad_pais('buenos aires', 'argentina', 3_000_000)
		self.assertEqual(salida, 'Buenos Aires, Argentina - 3000000 habitantes')

if __name__ == '__main__':
	unittest.main()