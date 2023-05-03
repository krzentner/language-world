

if check("the robot's gripper is not below the button"):
    robot.put("gripper above button")
if check("the robot's gripper is below the button"):
    robot.push("on the button")