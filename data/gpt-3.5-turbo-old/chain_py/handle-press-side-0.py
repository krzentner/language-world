# Steps:
#  1. Put gripper above the handle
#  2. Grab the handle with the gripper
#  3. Push down on the handle from the side
# First, put the gripper roughly above the handle.
if check("the robot's gripper is not above the handle"):
    robot.place("gripper above handle")
# If the gripper isn't around the handle, put it around the handle.
if check("the robot's gripper is not around handle and the robot's gripper is open"):
    robot.drop("gripper around handle")
# If the gripper is around the handle, we can push down on it from the side.
if check("the robot's gripper is around handle"):
    robot.push("down on handle from the side")