# Steps:
    #  1. Put the gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench isn't in the gripper, try to grab it.
    if check("the robot's gripper is above the wrench and the wrench is not in the gripper"):
        robot.move_gripper("around the wrench")
    # Once the gripper has the wrench, pull it off the peg.
    if check("the wrench is in the gripper"):
        robot.move_gripper("up and away from the peg")