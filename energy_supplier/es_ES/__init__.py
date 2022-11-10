# -*- coding: utf-8 -*-

import random
from random import choice
from re import match

from energy_supplier import BaseEnergySupplier
from faker.providers import ElementsType

localized = True

class EnergySupplier(BaseEnergySupplier):

	distributor: ElementsType[str] = \
		(
		"0023",
		"0024",
		"0029",
		"0288",
		"0363",
		"0396",
		"0021",
		"0022",
		"0390",
		"0397",
		"0026",
		"0027"
		)

	country_code = "ES"

	def code(self, point_type):
		"""
		Returs a random code based on CUPS https://es.wikipedia.org/wiki/C%C3%B3digo_Unificado_de_Punto_de_Suministro
		"""
		cups16 = self.distributor[random.randrange(0, len(self.distributor)-1)] \
			   + str(self.numerify("############"))
		control = self.calculate_control_code(cups16)

		if point_type== "F":
			return self.country_code + cups16 + control + "1F"
		elif point_type== "P":
			return self.country_code + cups16 + control + "1P"
		elif point_type== "C":
			return self.country_code + cups16 + control + "1C"
		elif point_type== "X":
			return self.country_code + cups16 + control + "1X"
		else:
			return self.country_code + cups16 + control
