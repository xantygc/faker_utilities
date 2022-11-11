# -*- coding: utf-8 -*-

from faker.providers import BaseProvider
from random import choice


class Fare(BaseProvider):
    fare_list = {
        'power':
            [
                "3.0",
                "3.1",
                "6.2",
                "6.3",
                "6.4",
                "6.5",
                "6.1A",
                "6.1B",
                "2.0DHS",
                "2.1DHS",
                "2.0A",
                "2.0DHA",
                "2.1A",
                "2.1DHA"
            ],
        'gas':
            [
                "TUR1",
                "TUR2",
                "TUR3"
            ]
    }

    def power(self):
        return choice(self.fare_list["power"])

    def gas(self):
        return choice(self.fare_list["gas"])