
    # Steps:
    #  1. Line up wrench and peg from point of view above
    #  2. Push down to ensure the wrench is around the peg
    #  3. Ensure the wrench is secure around the peg
    # To line up the wrench and the peg, we need to make sure the robot's
    # gripper is covering the peg from above.
    if check("the robot's gripper is not above the peg and the wrench is not above the peg"):
        robot.move_gripper("above the peg")
    # As long as the wrench is not around the peg, we can push down to secure
    # the wrench to the peg.
    if check("the robot's gripper is not around the robot"):
        robot.move_gripper("above the peg", close_gripper=True)
    # Once the wrench is around the peg and the robot's grip is closed, make
    # sure the wrench is secure.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the peg")