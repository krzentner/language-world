
    # Step:
    #  1. Line up the hammer head and the nail
    #  2. Hit the nail with the hammer
    # First, we need to get the hammer head lined up with the nail.
    if check("the hammer head and nail are not aligned"):
        robot.move_gripper("aligned with nail and hammer head")
    # Then, we hit the nail with the hammer.
    if check("the hammer head and nail are aligned"):
        robot.move_gripper("hit the nail")