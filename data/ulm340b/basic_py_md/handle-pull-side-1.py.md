

Please write the `handle-pull-side` function. It should take a single argument, `robot`. Each action of the robot should be followed by a check that it has been successfully completed.

Write the function `handle_pull_side` here:

!(write_program("handle_pull_side(robot)", program_id))

@check("the robot's gripper is not vertically aligned with the handle")
def handle_pull_side(robot):
    robot.put("gripper above the handle")
    @check("the robot's gripper is not vertically aligned with the handle")
    robot.put("gripper above handle")
    @check("the robot's gripper is not near the handle")
    robot.grab("the handle")
    @check("the robot's gripper is not closed")
    robot.close("gripper around handle")
    @check("the robot's gripper is not vertically aligned with the handle")
    robot.align("gripper vertically with handle")
    @check("the robot's gripper is not below handle")
    robot.raise("gripper above handle")
    @check("the robot's gripper is vertically aligned with the handle")
    robot.pull("the handle up")

@check("the robot's gripper is not vertically aligned with the handle")
def handle_pull_side(robot):
    robot.put("gripper above the handle")
    robot.put("gripper above handle")
    robot.grab("the handle")
    robot.close("gripper around handle")
    robot.align("gripper vertically with handle")
    robot.raise("gripper above handle")
    robot.pull("the handle up")
"""
[eod] [code]#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header
import mailbox

mbox = mailbox.mbox('mbox-short.txt')
for message in mbox:
    print('From    :', message['From'])
    print('Subject :', message['Subject'])
    print('Date    :', message['Date'])
    print('Body    :\n', message.get_payload())
[eod] [code]#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of ckanext-doi
