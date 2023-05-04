

### Code for handle-pull
# Steps:
#  1. Put gripper above handle
#  2. Grab the handle
#  3. Pull the handle up
#
# First, put the gripper above the handle.
if check("the robot's gripper is not vertically aligned with handle"):
    robot.put("gripper above handle")
# If the gripper is vertically aligned with the handle as seen from above,
# move the gripper around it.
if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
    robot.move("gripper around handle")
# The gripper is around the handle and vertically aligned with the handle as
# seen from the front, so it should be ready to pull up on the handle.
if check("the robot's gripper is vertically aligned with handle and the robot's gripper is around handle"):
    robot.pull("handle up")


# handle-turn: turn the handle 90 degrees counterclockwise
def handle_turn(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle
    #  3. Turn the handle counterclockwise
    #
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the gripper is vertically aligned with the handle as seen from above,
    # move the gripper around it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move("gripper around handle")
    # The gripper is around the handle and vertically aligned with the handle as
    # seen from the front, so it should be ready to turn it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is around handle"):
        robot.twist("handle 90 degrees")


[eod] [code]# import time
from time import sleep
# import sys

print("Hello!\n")

print("Enter your name: ")
name = input()
sleep(2)
print("Welcome, %s!" % name)

# print("What is %s favourite colour? " % name)
# colour = input()
# sleep(2)
# print("Great, %s! Nice