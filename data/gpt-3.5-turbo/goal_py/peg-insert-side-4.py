# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    # We're assuming that the peg is not already in the gripper.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is above the peg but not around it, move it around the peg
    # and close the gripper to grab it.
    if check("the robot's gripper is above the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg but not aligned with the hole, align it
    # with the hole.
    if check("the robot's gripper is around the peg and the peg is not horizontally aligned with the hole"):
        robot.move_gripper("horizontally aligned with the hole")
    # If the gripper is aligned with the hole, slide the peg in.
    if check("the robot's gripper is forward aligned with the peg and the peg is horizontally aligned with the hole"):
        robot.move_gripper("horizontally aligned with the hole and the peg is inside the hole")