

Here is a picture to show how to move the ball into the hoop:

![alt_text](basketball.png "A picture showing how to move the ball into the hoop.")

Please make sure your code runs successfully. Press the "Check Code" button when you are done.

"""
    
if 'train' in data:
    train(data, ['basketball.png'], {'robot': robot})
    
if 'final_eval' in data:
    final_eval(data, ['basketball.png'], {'robot': robot})
    
if 'eval' in data:
    eval(data, ['basketball.png'], {'robot': robot})
    
if 'test' in data:
    test(data, ['basketball.png'], {'robot': robot})
    
if 'task' in data:
    if 'basketball' in data['task']:
        start_pos = data['task']['basketball']['goal']
        basketball(robot, 2.3, 0.95, start_pos)
[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Shiboken Python Bindings Generator project.
#
# Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
#
# Contact: PySide team <contact@pyside.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation. Please
# review the following information to ensure the GNU Lesser General
# Public License version 2.1 requirements will be met:
# http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
# #
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

'''Test cases for object with QHash as member'''

import sys
