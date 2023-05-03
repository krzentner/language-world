

Steps:
1. Put gripper beside the handle
2. Push down on the handle

if check("the robot's gripper is not sideways aligned with handle"):
    robot.put("gripper beside handle")

if check("the robot's gripper is sideways aligned with the handle"):
    robot.push("down on handle")