

"""

def check(state):
    return False


def coffee_button(robot):
    """Push the button on the coffee machine."""
    if check("the robot's gripper is above the drawer handle and the robot's gripper is not below the drawer handle"):
        robot.put("the gripper below the drawer handle")
    if check("the robot's gripper is above the drawer handle and the robot's gripper is below the drawer handle"):
        robot.push("the drawer closed")
    if check("the robot's gripper is above the button and the robot's gripper is not below the button"):
        robot.push("the gripper below the button")
    if check("the robot's gripper is above the button and the robot's gripper is below the button"):
        robot.push("down on the button")


if __name__ == '__main__':
    coffee_button(0)[eod] [code]#!/usr/bin/env python3
#
# Copyright 2016-2021 Michael R. Hoopmann All Rights Reserved
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
#
# pylint: disable=pointless-string-statement


"""
https://github.com/nhl/
"""


__all__ = [
    'NHLPlayer',
    'NHLGame',
    'NHLTeam',
    'NHLTeamSchedule',
    'NHLStandings'
]


import re
import time

import http_api


class NHLPlayer(http_api.HTTPAPI):
    """
    Parses an NHL player.
    """

    def __init__(self, uri):
        http_api.HTTPAPI.__init__(self, uri)
        self._data = None

    @property
    def last_name(self):
        """
        Returns:
           str: the player's last name.
        """
        if not self._data:
