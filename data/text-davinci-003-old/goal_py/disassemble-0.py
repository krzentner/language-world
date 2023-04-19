
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench isn't below the gripper as seen from above, move the gripper
    # above the wrench.
    if check("the robot's gripper is not around wrench and the robot's gripper is open"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # If the gripper is around the wrench, we can just pull the wrench off the
    # peg.
    if check("the robot's gripper is around wrench"):
        robot.move_gripper("above the peg")