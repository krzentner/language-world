
    # Steps:
    #  1. Put gripper near the wrench
    #  2. Grab the wrench
    #  3. Pull the wrench off the peg
    # First, move the gripper near the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # If the robot's gripper is close to the wrench, grab it by closing the
    # gripper.
    if check("the robot's gripper is near the wrench and the robot's gripper is closed"):
        robot.move_gripper("right of the wrench")
    # Now that the wrench is in the gripper, just pull it off the peg.
    if check("the robot's gripper is not right of the wrench and the robot's gripper is closed"):
        robot.move_gripper("near the wrench")