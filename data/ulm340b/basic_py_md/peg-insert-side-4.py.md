
"""

# The following is a completed program, but it does not need to match the student's solution.
# Use this to check your unit tests.
# This program includes the task from the tutorial to make testing easier

def reach_up(robot):
    robot.move("to goal")

def move_to_gripper_left(robot):
    if check("the gripper is right of the goal"):
        robot.move("the gripper to left of the goal")

def move_to_gripper_right(robot):
    if check("the gripper is left of the goal"):
        robot.move("the gripper to right of the goal")

def move_gripper_forward(robot):
    if check("the gripper is not forward of the goal"):
        robot.move("the gripper forward of the goal")

def drop_gripper(robot):
    if check("the gripper is not down"):
        robot.move("gripper down")

def push_gripper_down(robot):
    if check("the gripper is not down"):
        robot.move("gripper down")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

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
    if check("the robot's gripper is forward aligned with drawer