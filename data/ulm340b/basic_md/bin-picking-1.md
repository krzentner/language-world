
"""


def get_instruction(task, task_data=None):
    task = task.strip()
    if task == "button-press-topdown":
        message = BUTTON_PRESS_TOPDOWN_MESSAGE
    elif task == "drawer-open":
        message = DRAWER_OPEN_MESSAGE
    elif task == "drawer-close":
        message = DRAWER_CLOSE_MESSAGE
    elif task == "door-open":
        message = DOOR_OPEN_MESSAGE
    elif task == "window-open":
        message = WINDOW_OPEN_MESSAGE
    elif task == "window-close":
        message = WINDOW_CLOSE_MESSAGE
    elif task == "reach":
        message = REACH_MESSAGE
    elif task == "push":
        message = PUSH_MESSAGE
    elif task == "pick-place":
        message = PICK_PLACE_MESSAGE
    elif task == "peg-insert-side":
        message = PEG_INSERT_SIDE_MESSAGE
    else:
        message = BIN_PICKING_MESSAGE
    return message
[eod] [code]from distutils.core import setup

setup(
    name = "openpay",
    version = "0.0.1",
    packages = ["openpay"],
    scripts = ["bin/openpay"],
    description = "Openpay Python API",
    author = "Openpay",
    author_email = "dev@openpay.mx",
    url = "https://github.com/openpay/openpay-python",
    license = "LICENSE.txt",
    download_url = "https://github.com/openpay/openpay-python/archive/v0.0.1.tar.gz"
)
[eod] [code]# Copyright 2022 AI Singapore
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest

from peekingduck.pipeline.nodes.dataset.image.convert_images import ConvertImages
from peekingduck.utils.image import Image
from peekingduck.utils.tests.node_tests import check_node
