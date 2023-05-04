
    The task `button-press-wall-low` requires the robot to push the button from the front with a short wall in the way.
To push the button from the front with a short wall in the way reliably, what steps the robot should perform?
    The task `button-press-wall-tall` requires the robot to push the button from the front with a tall wall in the way.
To push the button from the front with a tall wall in the way reliably, what steps the robot should perform?

The task `button-press-short` requires the robot to push the button.
To push the button reliably, what steps the robot should perform?
    The task `button-press-med` requires the robot to push the button.
To push the button reliably, what steps the robot should perform?
    The task `button-press-long` requires the robot to push the button.
To push the button reliably, what steps the robot should perform?

'''


[eod] [code]from setuptools import setup, find_packages
import codecs
import os
import re
import sys

def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

if sys.argv[-1] == "publish":
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

packages = find_packages()

install_requires = ['numpy', 'scipy', 'cython', 'matplotlib']

setup(
    name = 'cgraph',
    packages = packages,
    version = find_version("cgraph", "__init__.py"),
    url = "https://github.com/dhhagan/cgraph",
    license = "MIT",
    author = "Daniel Hagen",