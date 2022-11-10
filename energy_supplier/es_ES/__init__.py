# -*- coding: utf-8 -*-

import random
from random import choice
from re import match

from energy_supplier import BaseEnergySupplier
from faker.providers import ElementsType

localized = True


class PowerEnergySupplier(BaseEnergySupplier):
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

    def code(self, point_type=None):
        """Returns a random code based on CUPS https://es.wikipedia.org/wiki/C%C3%B3digo_Unificado_de_Punto_de_Suministro"""

        cups16 = self.distributor[random.randrange(0, len(self.distributor) - 1)] + str(self.numerify("############"))
        control = self.calculate_control_code(cups16)
        return self.evaluate_type(point_type, self.country_code, cups16, control)


class GasEnergySupplier(BaseEnergySupplier):
    distributor: ElementsType[str] = \
        (
            "0201",
            "0203",
            "0210",
            "0211",
            "0212",
            "0213",
            "0214",
            "0219",
            "0229",
            "0204",
            "0205",
            "0206",
            "0208",
            "0209",
            "0225",
            "0207",
            "0217",
            "0218",
            "0220",
            "0221",
            "0222",
            "0223",
            "0224",
            "0226",
            "0227",
            "0230",
            "0228",
            "0234",
            "0236"
        )

    country_code = "ES"

    def code(self, point_type=None):
        """Returns a random code based on CUPS https://es.wikipedia.org/wiki/C%C3%B3digo_Unificado_de_Punto_de_Suministro"""

        cups16 = self.distributor[random.randrange(0, len(self.distributor) - 1)] + str(self.numerify("############"))
        control = self.calculate_control_code(cups16)
        return self.evaluate_type(point_type, self.country_code, cups16, control)
