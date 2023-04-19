# Steps:
    #  1. Put gripper above coffee button
    #  2. Push down on the coffee button
    # First, put the gripper roughly above the coffee button
    if check("the robot's gripper is not above the coffee button"):
        robot.place("gripper above coffee button")
    # Once the gripper is lined up above the coffee button, just push down on
    # the button.
    if check("the robot's gripper is above the coffee button"):
        robot.push("down on coffee button")