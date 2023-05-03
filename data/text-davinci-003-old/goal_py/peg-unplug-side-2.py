
    # Steps:
    #  1. Put gripper right of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out sideways
    # If the robot's gripper is not in front of the peg, we can move the
    # gripper forward to grab it.
    if check("the robot's gripper is not forward aligned with the peg and the robot's gripper is open"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # Once the gripper is lined up in front, we can try to pull the peg out.
    if check("the robot's gripper is forward aligned with the peg and the robot's gripper is closed"):
        robot.move_gripper("right of the peg")