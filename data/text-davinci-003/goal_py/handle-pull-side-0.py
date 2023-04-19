
    # Steps:
    #  1. Put gripper above the bottom of the handle
    #  2. Grab the handle with the gripper
    #  3. Lift the handle up
    # Put the gripper left of the handle. We don't need to worry about being
    # exact because this is just a side pull.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # If the gripper is not on the handle, put it on the handle.
    # Again, we don't need to worry about aligning the gripper, since this is a
    # side pull.
    if check("the robot's gripper is left of the handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Pull up on the handle, using the gripper as a lever.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")