
    if check("the robot's gripper is not vertical aligned with the button"):
        robot.put("gripper above the button")
    if check("the robot's gripper is mostly vertical aligned with the button and the robot's gripper is not near the button"):
        robot.push("gripper towards the button")
    if check("the robot's gripper is near the button"):
        robot.push("button down")