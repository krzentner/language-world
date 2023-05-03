
    # Steps:
    #  1. Put gripper right of button
    #  2. Put gripper above button
    #  3. Push gripper wall up against the button
    # First, move the gripper right of the button.
    # We don't need to line up the gripper with the button, since we will be
    # pushing the wall up against it.
    if check("the robot's gripper is not right of the button"):
        robot.put("gripper right of button")
    # Now, try to move the gripper above the button and push it against the
    # wall.
    # Note that we do not want the gripper to be fully above the button.
    if check("the robot's gripper is not almost vertically aligned with the button"):
        robot.put("gripper above button")
    # Now, press the wall against the button.
    # We don't need to worry about the angle of the wall and the button, since 
    # the wall is short compared to the button and shouldn't be skewed when
    # pressing against it.
    if check("the robot's gripper is almost vertically aligned with the button"):
        robot.press("wall against button")