
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # Put the gripper above wrench.
    if check("the robot's gripper is not vertically aligned with the wrench and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # Pull the wrench off the peg.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is closed"):
        robot.move_gripper("left of the peg")