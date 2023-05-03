# Steps:
    #  1. Put gripper near the peg
    #  2. Drop gripper around the peg
    #  3. Lift the peg out of the hole
    #  4. Move peg to target location

    # First, move the gripper near the peg, so we can drop it around the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # Once the gripper is near the peg, we can drop it around the peg and pick
    # it up.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Now that we've grabbed the peg, lift it out of the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the hole")
    # Finally, move the peg to the target location.
    if check("the robot's gripper is above the hole and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")