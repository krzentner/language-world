# Steps:
    #  1. Put gripper above the wrench peg
    #  2. Drop gripper around the wrench peg
    #  3. Close gripper around the wrench peg
    #  4. Pull the wrench off the peg
    # First, put the gripper above the wrench peg.
    if check("the robot's gripper is not vertically aligned with the wrench peg"):
        robot.move_gripper("vertically aligned with the wrench peg")
    # If the gripper is above the wrench peg, put it around the wrench peg
    # by moving the gripper down.
    if check("the robot's gripper is vertically aligned with the wrench peg and the robot's gripper is not around the wrench peg"):
        robot.move_gripper("around the wrench peg", close_gripper=True)
    # Once the gripper is around the wrench peg, we should be able to pull it
    # off by moving the gripper up and away from the peg.
    if check("the robot's gripper is around the wrench peg"):
        robot.move_gripper("above the wrench peg and slightly to the side")