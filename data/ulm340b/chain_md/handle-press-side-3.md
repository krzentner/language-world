
    Answer:
    Steps:  1. Line up gripper on top of the handle  2. Push the handle downwards
    First, put the gripper above the handle.
    - When the robot's gripper is not vertically aligned with handle, the robot should put gripper above handle.
    If the robot's gripper is vertically aligned with the handle, we can push the handle down.
    - When the robot's gripper is vertically aligned with handle, the robot should push handle downwards.
'''
[eod] [code]#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_acos_bgp_neighbor
description:
    - Define BGP neighbor parameters
author: A10 Networks 2021
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        type: str
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        type: str
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        type: str
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        type: str
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        type: int
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        type: int
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        type: str
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    neighbor:
        description:
        - "Field neighbor"
        type: dict
        required: False
        suboptions:
            peer_group:
                description:
                - "BGP Peer Group