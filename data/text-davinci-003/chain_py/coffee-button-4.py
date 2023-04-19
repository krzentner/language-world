
    # Steps:
    #  1. Put gripper near the button
    #  2. Push down on the button
    # First, put the gripper right next to the button.
    if check("the robot's gripper is not near button"):
        robot.grab("button")
    # We've pinned down the place of the button with the gripper, so now just
    # push down on it to press it.
    if check("the robot's gripper is near button"):
        robot.push("down on button")