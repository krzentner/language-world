

When you're ready, tell me the code you wrote by inputting it, line by line.
"""
def check(state):
    return False

def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move_gripper("near the drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.move_gripper("around the drawer handle")
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.move_gripper("above the peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):