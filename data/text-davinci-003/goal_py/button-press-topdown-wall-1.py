
    # Steps:
    #  1. Put the gripper within the margin along the wall
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # This is very similar to "button-press-topdown", but with a wall in the way.
    # We first need to move the gripper so that it is within the margin along the
    # wall.
    if check("the robot's gripper is not within the margin along the wall and the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Now that the gripper is near the wall, we can line it up as seen from
    # above.
    if check("the robot's gripper is within the margin along the wall"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Finally, push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")