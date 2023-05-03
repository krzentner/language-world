
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.put("gripper above coffee button")
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("coffee button")