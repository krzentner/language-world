
"""


def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # We need to get the gripper above the puck before we can push it.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# In[ ]:




[eod] [code]#!/usr/bin/python
#
# Copyright (c) 2018 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_redisfirewallrule
version_added: "2.8"
short_description: Manage Azure RedisFirewallRule instance.
description:
    - Create, update and delete instance of Azure RedisFirewallRule.

options:
    resource_group:
        description:
            - The name of the resource group.
        required: True
        type: str
    name:
        description:
            - The name of the redis cache.
        required: True
        type: str
    state:
      description:
        - Assert the state of the RedisFirewallRule.
        