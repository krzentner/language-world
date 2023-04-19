# Steps:
    #  1. Put gripper to the side of the wall with a clear view of the button
    #  2. Move the gripper in front of the button
    #  3. Push the button
    # To press the button through the wall, we need to first position the gripper
    # to the side of the wall where we have a clear view of the button.
    if check("the robot's gripper is not to the side of the wall with a clear view of the button"):
        robot.move("gripper to side of wall with clear view of button")
    # Once we have a clear view of the button, we can move the gripper in front
    # of it.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper in front of button")
    # Finally, we can push the button with the gripper.
    if check("the robot's gripper is in front of the button"):
        robot.push("button")