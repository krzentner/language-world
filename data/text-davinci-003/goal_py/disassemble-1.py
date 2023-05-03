
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Grab the wrench with the gripper.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Once the wrench is grabbed, just pull it off the peg.
    if check("the robot's gripper is almost horizontally aligned with the peg"):
        robot.move_gripper("right of the peg")