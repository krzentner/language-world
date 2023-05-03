
    if check("the robot's gripper is not verticlly aligned with the button of the coffee machine"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with the button and the button is not below the robot's gripper"):
        robot.align("gripper to button")
    if check("the button is below the robot's gripper"):
        robot.push("button")