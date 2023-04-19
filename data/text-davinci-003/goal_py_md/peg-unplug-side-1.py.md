
    # Steps:
    #  1. Put the gripper in front of the peg
    #  2. Grab the peg using the gripper
    #  3. Pull the peg out sideways
    # The first step is to put the gripper so that it's in front of the peg.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # Grab the peg with the gripper by moving towards it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # With the peg in the gripper, pull it out sideways.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("left of the peg")