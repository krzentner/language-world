from setuptools import setup
from setuptools import find_packages

setup(
    name='language-to-policies',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    )

