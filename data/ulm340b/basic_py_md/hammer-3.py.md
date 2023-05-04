

Your goal is to write code to control a robot to pick up the hammer, align it with the nail, and strike the nail.
There is no need for special handling in case the nail is stuck.
The robot's gripper can handle both the hammer and the nail.

When you are finished, your code should pass all unit tests.
It should also produce a reasonable behavior when tested with the interactive simulator.

**Notes:**

1. Do not write code to rotate the hammer.
The hammer will be already rotated into the correct orientation.

2. Your code must pass all unit tests.

3. The goal of this exercise is to see how easy it is to write programs for the robot.
Try to write a program with fewer than 10 conditionals.
"""

# hammer: hit the nail with the hammer
def hammer(robot):
    # TODO: write code here
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above the hammer")
    if check("the robot's gripper is near the hammer and the robot's gripper is open"):
        robot.close("gripper around hammer")
    if check("the robot's gripper is not horizontally aligned with the nail"):
        robot.align("hammer to nail")
    if check("the robot's gripper is not above nail"):
        robot.put("gripper above nail")
    if check("the robot's gripper is above nail"):
        robot.slide("the hammer down to hit the nail")
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.lift("the hammer away")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned