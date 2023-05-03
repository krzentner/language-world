# Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    #  3. If pushing the door didn't work, move the gripper left or right and try again.
    # If the gripper isn't near the door handle, move it there.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle but not around it, move it around it.
    if check("the robot's gripper is near the door handle and not around it"):
        robot.move_gripper("around the door handle", close_gripper=True)
    # Move the door closed. If it doesn't work, move the gripper a little to the
    # left or right and try again.
    while check("the door is not closed"):
        if check("the robot's gripper is left of the door handle"):
            robot.move_gripper("right of the door handle")
        elif check("the robot's gripper is right of the door handle"):
            robot.move_gripper("left of the door handle")
        else:
            robot.move_gripper("horizontally aligned with the door handle")