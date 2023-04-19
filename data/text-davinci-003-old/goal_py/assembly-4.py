
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Put the gripper around the wrench
    #  3. Put the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Now that the gripper is around the wrench, we can move the wrench around
    # the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("around the peg")