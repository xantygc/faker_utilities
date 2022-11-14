import unittest
from energy_supplier.es_ES import PowerEnergySupplierProvider as PowerEnergySupplierES
from energy_supplier.es_ES import GasEnergySupplierProvider as GasEnergySupplierES
from faker import Faker


class TestEnergySupplierES(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(PowerEnergySupplierES)
        self.fake.add_provider(PowerEnergySupplierES)

    def test_type_c(self):
        cups = self.fake.power_code("C")
        self.assertEqual("C", cups[-1], "not the same type of cups")

    def test_none(self):
        cups = self.fake.power_code()
        self.assertEqual(20, len(cups), "not the same length")