

If check("the robot's gripper is not above the button"):
    robot.put("gripper above the button")
if check("button is below the robot's gripper"):
    robot.locate("gripper on the button")
if check("the robot's gripper is above the button"):
    robot.push("button downwards")