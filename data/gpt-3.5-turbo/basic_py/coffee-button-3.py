if check("the robot's gripper is not near the coffee machine button"):
        robot.move("gripper to coffee machine button")
    if check("the robot's gripper is on top of the coffee machine button"):
        robot.push("coffee machine button")