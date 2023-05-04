
""".replace("\n", " ").strip()

TASK_DESCRIPTIONS = {
    "peg-insert-side": "grab the peg and insert it into the hole from the side",
}
[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-13
"""
Setup file for 'wechat_sender' package.
"""

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'requests >= 2.2.1',
    'redis >= 2.10.3',
    'pyparsing >= 2.0.2'
]

setup(name='wechat_sender',
      version='0.0.1',
      description='',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="wechat_sender",
      entry_points="""\
      [paste.app_factory]
      main = wechat_sender:main
      """,
      )
[eod] [code]from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World.")

def add_number(request):
    first_number = int(request.GET["first_number"])
    second_number = int(request.GET["second_number"])
    result = first_number + second_number
    html_data = str(result)
    return HttpResponse(html_data)

def multiply_number(request):
    first_number = int(request.GET["first_number"])
    second_number = int(request.GET["second