
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.put("gripper above the coffee button")
    if check("the robot's gripper is vertically aligned with the coffee button"):
        robot.push("down on the coffee button")