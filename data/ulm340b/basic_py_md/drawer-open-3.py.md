

Then, after careful consideration of the previous programs and this one, add a sequence of commands to it that accomplish the task.

"""

def drawer_open(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.push("drawer open harder")

##########################################
# GRADED PROBLEM 1: BUTTON-PRESS-SIDEWAYS
##########################################

# Here's a video of someone pressing a button sideways using the robot:

# https://www.youtube.com/watch?v=a_kR53v8bCw&t=2842s

# Here's some code that demonstrates how the robot can do a variety of tasks:

# def button_press_topdown(robot):
#     if check("the robot's gripper is not vertically aligned with button"):
#         robot.put("gripper above button")
#     if check("the robot's gripper is vertically aligned with button"):
#         robot.push("down on button")

# def drawer_close(robot):
#     if check("the robot's gripper is not near the drawer handle"):
#         robot.grab("drawer handle")
#     if check("the robot's gripper is forward aligned with drawer handle"):
#         robot.push("drawer closed")
#     if check("the robot's gripper is in front of the drawer handle"):
#         robot.push("drawer closed harder")

# def door_open(robot):
#     if check("the robot's gripper is not almost vertically aligned with door handle"):
#         robot.put("gripper above door handle")
#     if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
#         robot.put("gripper around door handle")
#     if check("the robot's gripper is vertically aligned with the door handle"):
#         robot.pull("door open")

# def peg_insert_side(robot):
#     if check("the robot's gripper is not vertically aligned with the peg"):
#         robot.put("gripper above peg")
#     if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot