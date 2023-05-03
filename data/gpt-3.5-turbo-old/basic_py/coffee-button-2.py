if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move("gripper above coffee machine button")
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.push("coffee machine button")