
    # Steps:
    #  1. Put gripper near the wall
    #  2. Push the wall down to press the button
    # We want to put the gripper near the wall so that it doesn't accidentally
    # push the button once we start pushing the wall.
    # We also want to make sure the front end of the gripper is near the
    # button because the wall will likely get in the way if it is not.
    if check("the robot's gripper is not in front of the button and the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall", close_gripper=True)
    # Now that the gripper is near the wall and button, push the wall towards
    # the button to press it.
    if check("the robot's gripper is near the wall"):
        robot.move_gripper("in front of the button")