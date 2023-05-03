# Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Move gripper away from the peg
    # First, put the gripper above the wrench, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # If the gripper isn't around the wrench, put it around the wrench.
    if check("the robot's gripper is not around the wrench and the robot's gripper is open"):
        robot.move_gripper("near the wrench", close_gripper=True)
    # Once the gripper is around the wrench, we can just pull it off the peg.
    if check("the robot's gripper is around the wrench and is not near the peg"):
        robot.move_gripper("left of the peg")