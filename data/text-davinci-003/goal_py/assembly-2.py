
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't left of the gripper, move the gripper so that it is.
    # Because the wrench is narrow, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench, line up the wrench
    # with the peg.
    if check("wrench is left of peg and wrench is not horizontally aligned with peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # Once the wrench is lined up with the peg, land the wrench around the peg.
    if check("the robot's gripper is horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")