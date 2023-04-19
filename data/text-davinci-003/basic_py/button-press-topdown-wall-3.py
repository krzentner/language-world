
    if check("the robot's gripper is not near the button"):
        robot.put("gripper above button")
    if check("the robot's gripper is near the button and the robot's gripper is not aligned above the button"):
        robot.move("gripper to the side of the button")
    if check("the robot's gripper is aligned above the button"):
        robot.move("wall out of the way")
    if check("the robot's gripper is aligned above the button and the wall is out of the way"):
        robot.push("down on the button")