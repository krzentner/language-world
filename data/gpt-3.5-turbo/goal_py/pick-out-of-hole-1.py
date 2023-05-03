# Steps:
    #  1. Center gripper above hole
    #  2. Lower gripper into hole, around peg
    #  3. Close gripper around peg
    #  4. Lift gripper out of hole
    #  5. Move gripper to target location
    # First, line up the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Next, lower the gripper into the hole around the peg.
    if check("the robot's gripper is vertically aligned with the hole and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper has closed around the peg, lift it out of the hole.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("vertically aligned with the hole")
    # Finally, move the gripper to the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location", close_gripper=True)