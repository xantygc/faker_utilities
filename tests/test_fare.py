from unittest import TestCase
from faker import Faker
from fare.es_ES import Fare


class TestFare(TestCase):
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

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(Fare)

    def test_power(self):
        fare = self.fake.power();
        self.assertIn(fare, self.fare_list["power"])

    def test_gas(self):
        fare = self.fake.gas();
        self.assertIn(fare, self.fare_list["gas"])