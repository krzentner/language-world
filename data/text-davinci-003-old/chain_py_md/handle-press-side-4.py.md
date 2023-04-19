

Steps:
1. Put gripper to the side of the handle
2. Push down on the handle

if check("the robot's gripper is not side aligned with the handle"):
    robot.put("gripper to the side of the handle")
if check("the robot's gripper is side aligned with the handle"):
    robot.push("down on the handle")