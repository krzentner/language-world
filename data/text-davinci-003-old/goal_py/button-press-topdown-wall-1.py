
    # Steps:
    #  1. Put gripper above the short wall
    #  2. Move gripper above the button
    #  3. Push down on the button from the top
    # First, put the gripper above the short wall.
    if check("the robot's gripper is not above the wall"):
        robot.move_gripper("above the wall")
    # Next, we need to line up the gripper with the button as viewed from
    # above.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("near the button")