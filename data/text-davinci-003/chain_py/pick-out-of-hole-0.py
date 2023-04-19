
    # Steps:
    #  1. Put gripper horizontally above hole
    #  2. Drop gripper vertically into hole
    #  3. Align the gripper with the peg
    #  4. Grab the peg with the gripper
    #  5. Lift the peg up out of the hole
    # First, put the gripper above the hole, so that we don't bump it while
    # trying to grab the peg.
    if check("the robot's gripper is not horizontally aligned with hole"):
        robot.put("gripper above hole")
    # If the gripper is lined up with the hole from above, drop the gripper into
    # the hole.
    if check("the robot's gripper is horizontally aligned with the hole and the robot's gripper is not in the hole"):
        robot.drop("gripper into the hole")
    # Once the gripper is in the hole, move it around until it's lined up with
    # the peg.
    if check("the robot's gripper is in the hole and the robot's gripper is not aligned with the peg"):
        robot.align("gripper with peg")
    # If the peg is aligned with the gripper, grab it.
    if check("the robot's gripper is aligned with the peg"):
        robot.grab("peg")
    # Now that we have the peg, raise the gripper out of the hole.
    if check("the robot's gripper is aligned with the peg and the robot's gripper is in the hole"):
        robot.lift("peg out of hole")