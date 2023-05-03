
    # Steps:
    #  1. Put the gripper above the button
    #  2. Push down on the button
    # First, put the gripper above the button, as this will be the most precise
    # way to line up the robot's gripper with the button.
    if check("the robot's gripper is not above the button"):
        robot.place("gripper above button")
    # Once the gripper is roughly aligned above the button, try pushing down on
    # it.
    if check("the robot's gripper is above the button"):
        robot.push("down on button")