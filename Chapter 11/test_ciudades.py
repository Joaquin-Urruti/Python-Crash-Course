import unittest
from ciudad_funciones import ciudad_pais

class CiudadTestCase(unittest.TestCase):
	"""Pruebas para la funcion ciudad_pais"""
	def test_ciudad_pais(self):
		"""Probar si funciona el formateador"""
		ciudad_formateada = ciudad_pais('buenos aires', 'argentina')
		self.assertEqual(ciudad_formateada, 'Buenos Aires, Argentina')

if __name__ == '__main__':
	unittest.main()