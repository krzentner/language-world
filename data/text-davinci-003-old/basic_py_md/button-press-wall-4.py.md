

if check("the robot's gripper is not near the wall"):
    robot.put("gripper against wall")
if check("the robot's gripper is near the wall and the robot's gripper is not vertically aligned with the button"):
    robot.put("gripper in front of button")
if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
    robot.push("gripper against button")
if check("the robot's gripper is near the button"):
    robot.push("button with short wall in the way")