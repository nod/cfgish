
from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_descr = open(path.join(here, "README.md")).read()

setup(
    name = 'cfgish',
    version = '0.0.1',
    description = 'simplify sane configuration',
    url = 'https://github.com/nod/cfgish',
    author_email = 'jeremy@33ad.org',
    license = 'MIT',
    classifiers = [ 'Development Status :: 3 - Alpha' ],
    packages = ['cfgish'],
    package_dir = {'':'src'},
    pakage_data = {},
    install_requires = [ ]
)



