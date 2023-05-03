
    # Steps:
    #  1. Put gripper left of drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push close the drawer
    # It would be awkward to start by putting the gripper above the drawer
    # handle, so we start by putting it to the left of the handle.
    if check("the robot's gripper is not left of drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # As long as the gripper is around the drawer handle, move the gripper right
    # to push the drawer closed.
    if check("the robot's gripper is around drawer handle and the robot's gripper is not right of the drawer handle"):
        robot.move_gripper("right of the drawer handle")