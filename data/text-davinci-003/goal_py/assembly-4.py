
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Push the wrench onto the peg
    # To put the wrench around the peg, we first need to make sure the wrench is
    # lined up above the peg.
    if check("the wrench is not above the peg"):
        robot.move_gripper("above the wrench")
    # Then, start pushing the wrench onto the peg by moving the gripper
    # downwards.
    if check("the robot's gripper is above the wrench and the wrench is below the peg"):
        robot.move_gripper("above the peg")
    # If the wrench is too far away, move sideways until the wrench is lined up
    # with the peg.
    if check("the robot's gripper is at the same height as the peg and the wrench is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")