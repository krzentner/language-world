
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("into drawer")

# turn-off: press the button down to turn it off
def turn_off(robot):
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above the button"):
        robot.press("down on button")

# turn-on: press the button down to turn it on
def turn_on(robot):
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is above the button"):
        robot.press("down on button")

# button-press-side: push the button down from the side
def button_press_side(robot):
    if check("the robot's gripper is not aligned with the button"):
        robot.put("gripper next to button")
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("into button")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")
[eod] [code]class CompositorNodeMapUV:

    def update(self):
        pass



[eod] [code]'''
1310. XOR Queries of a Subarray
Given an array arr of size N and Q queries denoting a range [L, R] for each query, your task is to compute the XOR for all the elements in the range [L, R] for each query and return the answer.

Input Format:
First-line will contain the number N, denoting