
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Line the wrench up with the peg
    #  4. Wrap the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the wrench becomes forward of the gripper, go back to putting the 
    # gripper above the wrench.
    # Because the wrench is a wide object, check if the gripper is lined up with
    # it from left or right instead of around it.
    if check("the wrench is not left of the robot's gripper and the wrench is not right of the robot's gripper"):
        robot.move_gripper("left of the wrench", close_gripper=True)
    # As long the wrench is behind the robot's gripper, line up the wrench with the
    # peg.
    if check("the wrench is forward aligned with the peg"):
        robot.move_gripper("right of the wrench")
    # When the wrench is lined up with the peg, wrap it around the peg by 
    # pushing it down.
    if check("the robot's gripper is left of the wrench and the wrench is not around the peg"):
        robot.move_gripper("below the peg")