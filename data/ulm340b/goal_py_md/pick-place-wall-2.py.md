
"""


# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
[eod] [code]#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

from .builder import HEADS


@HEADS.register()
class DenseHead(nn.Layer):
    """
    The class for the dense branch of HRNet.
    """
    def __init__(self, in_channels, norm_type='BN', norm_decay=0.,
                 act_type='prelu', act_param=0.01):
        """
        Initialize the class with the shape of the input and other parameters.

        Args:
            in_channels (int): The number of input channel.
            norm_type (str, optional): The type of normalizaton layer to use.
            norm_decay (float, optional): The weight decay of normalizaton layer.
            act_type (str, optional): The type of activation layer to use.
            act_param (int, optional): The parameter of activation layer to use.

        Returns:
            None
        """
        super(DenseHead, self).__init__()
        self.in_channels = in_channels
        self.act = act_type
        self.norm_type =