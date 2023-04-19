

Steps:
1. Put gripper above the handle
2. Drop gripper around the handle
3. Pull the handle up

if check("the robot's gripper is not vertically aligned with the handle"):
    robot.put("gripper above the handle")
if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
    robot.drop("gripper around the handle")
if check("the robot's gripper is around the handle"):
    robot.pull("handle up")