
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Pull the peg sideways out of the hole
    # Start by putting the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # Once the gripper is above the peg, we can grab it by moving the gripper
    # down around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, line up the peg with the hole.
    if check("the peg is horizontally aligned with the hole"):
        robot.move_gripper("above the peg")
    # Once the peg is lined up with the hole, pull it out.
    if check("the robot's gripper is forward aligned with the peg and the peg is horizontally aligned with the hole"):
        robot.move_gripper("horizontally aligned with the hole")