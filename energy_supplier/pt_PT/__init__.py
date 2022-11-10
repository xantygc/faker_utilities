# -*- coding: utf-8 -*-

from random import choice
from faker.providers import BaseProvider, ElementsType

localized = True

class EnergySupplier(BaseProvider):

	distributor: ElementsType[str] = ()
	country_code = "PT"

	def code(self):
		"""
		Returs a random code based on CUPS or EIC
		"""
		return self.country_code + str(self.random_element(7, True))