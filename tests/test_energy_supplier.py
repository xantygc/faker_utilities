import unittest
from energy_supplier.es_ES import EnergySupplier as EnergySupplierES
from faker import Faker

class TestEnergySupplierES(unittest.TestCase):

	def setUp(self):
		self.fake = Faker()
		self.fake.add_provider(EnergySupplierES)

	def test_1(self):

		print(self.fake.code("C"))