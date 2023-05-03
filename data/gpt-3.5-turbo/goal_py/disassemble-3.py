# Steps:
    #  1. Put gripper above wrench
    #  2. Grab the wrench with the gripper
    #  3. Pull the wrench off the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not above wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench already, move it around the wrench
    # by closing the gripper.
    if check("the robot's gripper is not around wrench"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Once the gripper is around the wrench, pull the wrench off the peg by
    # moving the gripper upwards.
    if check("the robot's gripper is around wrench"):
        robot.move_gripper("above the peg")