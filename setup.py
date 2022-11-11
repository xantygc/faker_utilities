#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup, find_packages
from glob import glob
from os.path import splitext, basename, abspath, dirname, join

here = abspath(dirname(__file__))
try:
    README = open(join(here, 'README.md')).read()
except:
    README = 'An add-on provider for the Python Faker module to generate random CUPS (Universal Supply Point Code) or other useful topics for utilities sector processes. See ' \
             'https://github.com/xantygc/faker_utilities. '

CLASSIFIERS = [
    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Unix',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Utilities',
]

setup(
    name='faker_utilities',
    version='0.1.0',
    license='MIT',
    description='Provider of energy & utilities topics data for Faker module',
    author='Santiago González',
    author_email='santiago.gonzalez.courel@gmail.com',
    url='https://github.com/xantygc/faker_utilities',
    long_description=README,
    packages=find_packages('energy_supplier'),
    package_dir={'': 'energy_supplier'},
    py_modules=[splitext(basename(path))[0] for path in glob('energy_supplier/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    project_urls={
        'Bug Tracker': 'https://github.com/xantygc/faker_utilities/issues',
    },
    python_requires='>=3.6',
    install_requires=['Faker>=8.2.1']
)