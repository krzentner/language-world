

If check("the robot's gripper is not vertically aligned with the button"):
    robot.put("gripper in front of button")
if check("the robot's gripper is not near the button"):
    robot.move("gripper to left of button")
if check("the robot's gripper is to left of button"):
    robot.move("gripper to right of button")
if check("the robot's gripper is aligned with the button's wall"):
    robot.push("gripper against wall")
if check("the robot's gripper is in front of the button"):
    robot.push("button")