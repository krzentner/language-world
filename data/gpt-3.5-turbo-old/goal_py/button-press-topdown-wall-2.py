# Steps:
    #  1. Move the gripper to the side to avoid the wall
    #  2. Line up the gripper as viewed from above
    #  3. Push down on the button from the top
    # Because there's a wall in the way, we need to move the gripper to the side
    # so that it can approach the button from above.
    if check("the gripper is not to the side of the button"):
        robot.move_gripper("to the side of the button")
    # Once the gripper is in position, line it up from above with the button and
    # push down on the button.
    if check("the gripper is to the side of the button and vertically aligned with the button"):
        robot.move_gripper("near the button")