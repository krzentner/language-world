
    # Steps:
    #  1. Move the gripper near the wrench
    #  2. Put the gripper around the wrench
    #  3. Pull the wrench off the peg
    # First, move the gripper to the wrench.
    if check("the robot's gripper is not near the wrench"):
        robot.move_gripper("near the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Once the gripper is around the wrench, we can just pull the wrench off the
    # peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("above the peg")