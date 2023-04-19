# Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't in the gripper yet, grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is not around the wrench"):
        robot.move_gripper("around the wrench")
    # Once the wrench is in the gripper, pull it off the peg.
    if check("the robot's gripper is around the wrench"):
        robot.move_gripper("away from the peg")