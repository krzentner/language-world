# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench so that we can grab it.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Once the gripper is above the wrench, close the gripper to grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not closed"):
        robot.move_gripper("around the wrench")
    # Once the gripper is closed around the wrench, we should be able to pull
    # the wrench off the peg.
    if check("the robot's gripper is closed around the wrench and the wrench is still on the peg"):
        robot.move_gripper("left of the wrench")