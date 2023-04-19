
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push the wall so that the button is exposed
    #  3. Push down on the buttononce it's exposed
    # The robot needs to line up its gripper with the button by looking at it
    # from above.
    # To do that, the robot will need to see if there's an obstacle blocking the
    # button, that is, the short wall.
    if check("there is a short wall in the way of the robot's gripper and button"):
        robot.move_gripper("forward aligned with the short wall")
    # The robot should push the wall until it's out of the way or curved around the button.
    if check("the wall is out of the way of the robot's gripper and button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the button is exposed, the robot can push it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")