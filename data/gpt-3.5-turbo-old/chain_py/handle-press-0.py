# Steps:
#  1. Line up gripper vertically with handle
#  2. Grab handle with gripper
#  3. Push down on handle
# First, put the gripper above the handle, vertically aligned with it.
if check("the robot's gripper is not vertically aligned with the handle"):
    robot.put("gripper above handle")
# If the gripper is above the handle, try to close the gripper around it.
if check("the robot's gripper is vertically aligned with handle and the robot's gripper is open"):
    robot.grab("handle")
# If the gripper is around the handle, push down on it.
if check("the robot's gripper is around handle"):
    robot.push("down on handle")