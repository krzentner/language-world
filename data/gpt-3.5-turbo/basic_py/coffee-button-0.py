if check("the robot's gripper is not near the coffee machine button"):
        robot.move("gripper to button")
    if check("the robot's gripper is near the coffee machine button"):
        robot.push("coffee button")