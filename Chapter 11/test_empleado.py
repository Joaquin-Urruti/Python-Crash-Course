import unittest
from ch11_p248_113_empleado import Empleado

class TestEmpleado(unittest.TestCase):
	"""Pruebas para la clase Empleado"""

	def setUp(self):
		"""Crea una instancia de un empleado para correr las pruebas"""
		self.empleado = Empleado('juan', 'perez', 60000)

	def test_dar_aumento(self):
		self.empleado.dar_aumento()
		self.assertEqual(self.empleado.salario_anual, 65000)

	def test_dar_aumento_personalizado(self):
		self.empleado.dar_aumento(aumento=10000)

if __name__ == '__main__':
	unittest.main()