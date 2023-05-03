

if check("the robot's gripper is not vertically aligned with button"):
    robot.put("gripper above button")
if check("the robot's gripper is vertically aligned with button"):
    robot.push("down on button")