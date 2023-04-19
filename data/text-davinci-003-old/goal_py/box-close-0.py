
    # Steps:
    #  1. Pick up the lid
    #  2. Place the lid on the box
    # Pick up the lid.
    if check("the robot's gripper is not near lid"):
        robot.move_gripper("near the lid", close_gripper=True)
    # Place the lid on the box.
    if check("the robot's gripper is near lid"):
        robot.move_gripper("above the box")