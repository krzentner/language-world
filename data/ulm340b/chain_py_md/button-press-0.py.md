

and then follow the instructions in the example program.

The following code block is run when you press the "Run" button.
You should change what the code does when the button is pressed here.

```
if button_press_code_written is False:
    raise NotImplementedError
else:
    if not button_press_tested:
        button_press_tested = True
        """
        TODO:
        Write code to perform the task, using the `check` function to check
        conditions and the `robot` function to perform an action.
        See the examples above.
        """
        # Steps:
        #  1. Line up the gripper as viewed from the front
        #  2. Push in towards the button until it's pressed
        # Line up the robot's gripper from the front.
        if check("the robot's gripper is not horizontally aligned with button"):
            robot.put("gripper in front of button")
        # Now that the gripper is lined up, just push the button.
        if check("the robot's gripper is horizontally aligned with button and the button is not being pressed"):
            robot.push("in towards the button")
```
'''

# TODO:
# Write code to perform the task, using the `check` function to check
# conditions and the `robot` function to perform an action.
# See the examples above.
# Steps:
#  1. Line up the gripper as viewed from the front
#  2. Push in towards the button until it's pressed
# Line up the robot's gripper from the front.
if check("the robot's gripper is not horizontally aligned with button"):
    robot.put("gripper in front of button")
# Now that the gripper is lined up, just push the button.
if check("the robot's gripper is horizontally aligned with button and the button is not being pressed"):
    robot.push("in towards the button")
[eod] [code]# coding: utf-8

"""
    crush-staff 平台接口（职员管理平台）

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetStaffListRequest(object):