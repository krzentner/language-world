
    # Steps:
    #  1. Put gripper above the wall
    #  2. Put gripper behind the wall
    #  3. Line up the gripper in front of the button
    #  4. Push the button
    # First, put the gripper above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # If the gripper is above the wall, move it behind the wall, so that we have
    # more room to move the wall itself.
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("behind the wall")
    # Now that the wall is out of the way, line up the gripper in front of the
    # button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("forward aligned with the button", close_gripper=True)
    # Now that the gripper is lined up with the button, we can just push the
    # button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")