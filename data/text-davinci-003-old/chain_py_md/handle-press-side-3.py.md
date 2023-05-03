

Steps
1. Put gripper right of the handle
2. Put gripper above the handle
3. Push down on the handle from the side

if check("the robot's gripper is not right of the handle"):
    robot.put("gripper right of handle")
if check("the robot's gripper is not vertically aligned with handle"):
    robot.put("gripper above handle")
if check("the robot's gripper is vertically aligned with handle"):
    robot.push("down on handle from side")