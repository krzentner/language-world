
    # Steps:
    #  1. Put gripper above peg
    #  2. Put wrench around peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg isn't left of the gripper, move the gripper back to above the
    # peg.
    if check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # If the peg is left of the robot's gripper, move the gripper around the peg
    # to put the wrench on it.
    if check("the peg is left of the robot's gripper"):
        robot.move_gripper("around the peg")