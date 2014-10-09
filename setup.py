#!/usr/bin/env python

from setuptools import setup

short_description = 'Robot Framework wrapper for faker, a fake test data generator'
try:
    description = open('README.rst').read()
except IOError:
    description = short_description

try:
    license = open('LICENSE').read()
except IOError:
    license = 'MIT License'

with open('CHANGES.rst') as f:
    changes = f.read()

classifiers = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
""".strip().splitlines()

setup(
    name='robotframework-faker',
    package_dir={'': 'robotframework-faker'},
    packages=['FakerLibrary'],  # this must be the same as the name above
    version='2.0.3',
    description=short_description,
    author='Guy Kisel',
    author_email='guy.kisel@gmail.com',
    url='https://github.com/guykisel/robotframework-faker',
    download_url='https://pypi.python.org/pypi/robotframework-faker',
    keywords=('robotframework testing '
              'test automation testautomation '
              'atdd bdd faker'),  # arbitrary keywords
    install_requires=['fake-factory', 'robotframework'],
    long_description=description + '\n\n' + changes,
    license='MIT',
    classifiers=classifiers,
    platforms='any'
)
