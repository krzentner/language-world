
"""
[eod] [code]#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=
"""
File       : DataDiscovery.py
Author     : Valentin Kuznetsov <vkuznet AT gmail dot com>
Description: Utils for dealing with data.
"""
# futures
from __future__ import print_function, division

# system modules
import os
import sys
import shutil
import platform
from uuid import uuid4

# local modules
from Utils.PythonVersion import PY3
from Utils.Decorators import Stopwatch

def copyfile(input_filename, output_filename):
    """Copy input file to an output location"""
    # make directory if needed
    directory = os.path.dirname(output_filename)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as err:
            print('Directory was not created, error: %s' % err)
            return False

    # copy file
    try:
        shutil.copy(input_filename, output_filename)
        if PY3:
            return True
        return 1
    except IOError as err:
        print('%s was not created, error: %s' % (output_filename, err))
        return False

def symlink(input_filename, output_filename):
    """Symlink input file to an output location"""
    # make directory if needed
    directory = os.path.dirname(output_filename)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as err:
            print('Directory was not created, error: %s' % err)
            return False

    # symlink file
    try:
        if platform.system() == 'Linux':
            os.symlink(input_filename, output_filename)
        elif platform.system() == 'Darwin':
            os.symlink(input_filename, output_filename, target_is_directory=False)
        if PY3:
            return True
        return 1
    except OSError as err:
        print('%s was not created, error: %s' % (output_filename, err))
        return False

def find(directory, regexp):
    """Finds all files matching the regexp and returns them as list"""
    paths = []
    for root, dirs,