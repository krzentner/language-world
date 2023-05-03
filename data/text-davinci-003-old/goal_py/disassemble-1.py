
    # Steps:
    #  1. Put gripper around wrench
    #  2. Pull wrench off peg
    # First, we need to get the gripper around the wrench.
    # This will be trickier than things like the door or drawer because the
    # wrench is a smaller, more precise object.
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Once the gripper is around the handle we can just pull the wrench off the
    # peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("away from peg")