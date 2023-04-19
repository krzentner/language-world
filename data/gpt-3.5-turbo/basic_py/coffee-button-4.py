if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.put("gripper above coffee machine button")
    if check("the robot's gripper is vertically aligned with coffee machine button"):
        robot.push("down on coffee machine button")