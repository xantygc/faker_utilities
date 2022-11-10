# -*- coding: utf-8 -*-

import random
import pandas
from faker.providers import BaseProvider

localized = False


class BaseMeasureProvider(BaseProvider):

    def range(self, start, end, tz='Europe/London', period='h'):
        values=[]
        range = pandas.date_range(start, end, tz=tz, freq=period).tolist()
        for date in range:
            value = {'datetime': date.isoformat(), 'value': random.randint(0, 100)}
            values.append(value)
        return values



