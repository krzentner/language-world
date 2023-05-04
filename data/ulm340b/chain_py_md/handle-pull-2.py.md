

In your program, you can use `robot.check(condition)` to check a condition,
`robot.put(obj_name, dest_name)` to put an object somewhere,
`robot.move(obj_name, dest_name)` to move an object to a destination,
`robot.open(obj_name)` to open an object,
`robot.close(obj_name)` to close an object, and
`robot.grab(obj_name)` to grab an object.

"""

def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop the gripper around the handle
    #  3. Pull the handle up

    if robot.check('the robot\'s gripper is not vertically aligned with the handle'):
        robot.put('gripper above the handle')
    if robot.check('the robot\'s gripper is not around the handle and the robot\'s gripper is open'):
        robot.drop('gripper around the handle')
    if robot.check('the robot\'s gripper is around the handle'):
        robot.pull('the handle up')

def main():
    print("Beginning of the program")
    handle_pull(robot)
    print("End of the program")

if __name__ == "__main__":
    main()
[eod] [code]# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""export checkpoint file into air/mindir/onnx models"""
import argparse
import numpy as np

from mindspore import Tensor, load_checkpoint, load_param_into_net, export
from mindspore import context

from src.models.yolov3 import Yolov3DarkNet53
from src.utils.logger import Logger
from src.data