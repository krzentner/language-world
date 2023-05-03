
    # Steps:
    #  1. Put gripper near the side of the button
    #  2. Push down the side of the button
    # If the gripper is not near the button, move it near the button.
    # Also make sure it is not closed, since it isn't grabbing anything.
    if check("the robot's gripper is not near the button and gripper is closed"):
        robot.enter("gripper near the side of the button")
    # Now, with the gripper near the side of the button, push the button.
    if check("gripper is near the side of the button and gripper is open"):
        robot.push("down on the side of the button")