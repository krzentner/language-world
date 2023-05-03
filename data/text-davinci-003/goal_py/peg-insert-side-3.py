
    # Steps:
    #  1. Put gripper near peg
    #  2. Close gripper around peg
    #  3. Move the gripped peg above the hole
    #  4. Insert peg into hole
    # First, move the gripper near the peg so that it can grab it.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # Once the gripper is near the peg, close it to grab it.
    if check("the robot's gripper is near the peg and the robot's gripper is not closed"):
        robot.move_gripper("near the peg", close_gripper=True)
    # With the peg in the gripper, move it above the hole.
    if check("the robot's gripper is closed and the peg is not above the hole"):
        robot.move_gripper("above the hole")
    # Once the peg is above the hole, insert it by slowly moving the robot's
    # gripper downward.
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("vertically aligned with the peg")