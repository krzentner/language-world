
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # Once the gripper is above the peg, close the gripper to grab it.
    if check("the robot's gripper is open and the robot's gripper is vertically aligned with peg"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the robot's gripper is now closed, line up the peg with the hole.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the side instead of above.
    if check("the robot's gripper is closed and the peg is not horizontally aligned with hole"):
        robot.move_gripper("horizontally aligned with hole")
    # If the peg is lined up, insert it into the hole.
    if check("the robot's gripper is closed and the peg is horizontally aligned with the hole"):
        robot.move_gripper("around the peg", close_gripper=True)