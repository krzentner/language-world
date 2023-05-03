if check("the robot's gripper is not above the coffee machine button"):
        robot.place("gripper above button")
    if check("the robot's gripper is above the button"):
        robot.push("the button down")