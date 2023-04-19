# Steps:
#  1. Put gripper over handle
#  2. Push down on handle
# First, put the gripper over the handle.
if check("the robot's gripper is not over the handle"):
    robot.put("gripper over handle")
# Then, push down on the handle.
if check("the robot's gripper is over the handle"):
    robot.push("down on handle")