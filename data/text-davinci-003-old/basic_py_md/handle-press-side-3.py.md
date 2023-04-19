

if check("the robot's gripper is not horizontally aligned with the handle"):
    robot.put("gripper in front of the handle")
if check("the robot's gripper is horizontally aligned with the handle"):
    robot.push("gripper down on the handle")