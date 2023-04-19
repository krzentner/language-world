
    # Steps:
    #  1. Put gripper above the plate
    #  2. Move gripper onto the plate
    #  3. Slide the plate back
    # Line up the gripper with the plate from the top.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("around the plate")
    # We should grab the plate so that we don't knock it with the gripper while
    # we slide it back.
    if check("the robot's gripper is not around the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # Now that the gripper is grabbing the plate, move it.
    if check("the robot's gripper is around the plate"):
        robot.move_gripper("horizontally aligned with the target location")