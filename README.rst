=====================================
Faker Addon for Gas & Power Utilities
=====================================

|PyPI Package| |PyPI Python Versions| |Last Commit|

Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install faker_utilities

Generate a MEASURE range between dates:

.. code:: python

    self.fake = Faker()
    self.fake.add_provider(BaseMeasureProvider)
    fake.range(start=datetime.datetime(2022, 10, 30, 0, 0), end=datetime.datetime(2022, 10, 30, 23, 0), tz='Europe/Madrid', period='15min', min=100, max=50, decimals=6)

Spanish Power FARE:

.. code:: python

    faker = Faker()
    fake.add_provider(Fare)
    fare = fake.power()


.. |Last Commit| image:: https://img.shields.io/github/last-commit/xantygc/faker_utilities
   :target: https://pypi.org/project/faker-wifi-essid/
   :alt: PyPI Package Python Versions

.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/faker-utilities.svg?logo=python&style=flat
   :target: https://pypi.org/project/faker-wifi-essid/
   :alt: PyPI Package Python Versions

.. |PyPI Package| image:: https://img.shields.io/pypi/v/faker-utilities.svg?style=flat
   :target: https://pypi.org/project/faker-utilities/
   :alt: PyPI Package Latest Release
