
    # Steps:
    #  1. Put gripper above wrench handle
    #  2. Drop gripper around wrench handle
    #  3. Pull the wrench off the peg
    # As long as the wrench handle isn't laying flat against the peg, the robot
    # can just line up its gripper from above the wrench.
    if check("the robot's gripper is not vertically aligned with wrench handle"):
        robot.move_gripper("above the wrench handle")
    # If the wrench handle is laying flat against the peg, the robot has to
    # reach around the wrench to get its handle.
    if check("the robot's gripper is not around wrench handle and the robot's gripper is open"):
        robot.move_gripper("around the wrench handle", close_gripper=True)
    # Once the robot has a handle on the wrench, it can pull it off the peg.
    if check("the robot in front of the peg and the robot's gripper is closed"):
        robot.move_gripper("above the peg")