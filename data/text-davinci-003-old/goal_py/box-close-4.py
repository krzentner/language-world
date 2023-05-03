
    # Steps:
    #  1. Put gripper above the box lid
    #  2. Lower the gripper onto the box lid
    #  3. Pick up the lid
    #  4. Move the lid over the box
    #  5. Place the lid on the box
    # First, lift the gripper up near the box lid.
    if check("the robot's gripper is not near the box lid"):
        robot.move_gripper("near the box lid")
    # Now let's move the gripper down on the box lid.
    if check("the robot's gripper is above the box lid and the robot's gripper is not around the box lid"):
        robot.move_gripper("around the box lid", close_gripper=True)
    # We should be able to grab the lid if the gripper is around it.
    if check("the robot's gripper is around the box lid"):
        robot.move_gripper("above the box")
    # Now let's move the lid to the box.
    if check("the box lid is above the box and box lid is not aligned with the box"):
        robot.move_gripper("aligned with the box")
    # Finally, let's gently set the lid on the box.
    if check("the box lid is aligned with the box"):
        robot.move_gripper("near the box lid")