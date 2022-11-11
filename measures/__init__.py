# -*- coding: utf-8 -*-

import random
import pandas
from faker.providers import BaseProvider

localized = False


class BaseMeasureProvider(BaseProvider):

    def range(self, start, end, tz='Europe/London', period='h', min=0, max=100, decimals=2):
        values=[]
        range = pandas.date_range(start, end, tz=tz, freq=period).tolist()
        measures = {'start_datetime': start, 'end_datetime': end, 'timezone':tz, 'period': period, 'values': []}
        for date in range:
            value = {'datetime': date.isoformat(), 'value': round(random.uniform(min, max), decimals)}
            values.append(value)
        measures['values']=values
        return measures



