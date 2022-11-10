# -*- coding: utf-8 -*-

from random import choice
from faker.providers import BaseProvider, ElementsType

localized = True


class BaseEnergySupplier(BaseProvider):
    control_letters: ElementsType[str] = (
        "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")

    def calculate_control_code(self, cups16):
        cups16_mod = int(cups16) % 529
        quotient = int(cups16_mod / 23)
        remainder = cups16_mod % 23
        return self.control_letters[quotient] + self.control_letters[remainder]

    def evaluate_type(self, point_type, country_code, cups16, control):
        if point_type == "F":
            return country_code + cups16 + control + "1F"
        elif point_type == "P":
            return country_code + cups16 + control + "1P"
        elif point_type == "C":
            return country_code + cups16 + control + "1C"
        elif point_type == "X":
            return country_code + cups16 + control + "1X"
        elif point_type is None:
            return country_code + cups16 + control
        else:
            return None
