

This task involves picking up a cylinder that's on the floor and placing it in a hand that's on a desk.

You will want to call the function `check(statement)` to determine if a given statement is true or false. For example, `check("the robot's gripper is not above the puck")` will be True if the gripper is not above the puck and False if the gripper is above the puck.

There's one command to control the robot. You can call the function `robot.move(statement)` to make the robot perform a given action. For example, `robot.move("gripper to left of window handle")` will cause the gripper to move to the left of the window handle, if it isn't already there.

Please write a program that makes the robot perform the last task correctly.
"""

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle")