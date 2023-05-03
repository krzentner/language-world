
    # Steps:
    #  1. Put the gripper near the handle
    #  2. Push down on the handle
    #If the handle is not to the left of the gripper, move the gripper to the
    # handle so we can push down on it.
    if check("the handle is not left of the robot's gripper"):
        robot.move_gripper("left of the handle")
    # As long as the handle is to the left of the robot's gripper, keep pushing
    # the handle down
    if check("the handle is left of the robot's gripper and the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")