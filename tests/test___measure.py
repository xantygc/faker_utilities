import datetime
from unittest import TestCase
from faker import Faker
from measures import BaseMeasureProvider


class TestMeasure(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(BaseMeasureProvider)

    def test_range(self):
        measures = self.fake.range(start=datetime.datetime(2022, 1, 1, 0, 0), end=datetime.datetime(2022, 1, 1, 23, 0))
        self.assertEqual(24, len(measures['values']))

    def test_range_spain(self):
        measures = self.fake.range(start=datetime.datetime(2022, 10, 30, 0, 0), end=datetime.datetime(2022, 10, 30, 23, 0), tz='Europe/Madrid', min=100, max=50, decimals=6)
        self.assertEqual(25, len(measures['values']))

    def test_range_spain_15m(self):
        measures = self.fake.range(start=datetime.datetime(2022, 10, 30, 0, 0), end=datetime.datetime(2022, 10, 30, 23, 0), tz='Europe/Madrid', period='15min', min=100, max=50, decimals=6)
        self.assertEqual(97, len(measures['values']))
