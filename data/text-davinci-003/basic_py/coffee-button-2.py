
    if check("the robot's gripper is not near the button"):
        robot.put("gripper near coffee button")
    if check("the robot's gripper is near the coffee button and the robot's gripper is not around coffee button"):
        robot.grab("coffee button")
    if check("the robot's gripper is around the coffee button"):
        robot.push("coffee button in")