if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.move("gripper above coffee button")
    if check("the robot's gripper is vertically aligned with the coffee button and the robot's gripper is not touching the button"):
        robot.tap("coffee button")
    if check("the robot's gripper is touching the coffee button"):
        robot.push("down on coffee button")