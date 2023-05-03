# Steps:
    #  1. Position gripper to the side of the peg
    #  2. Move gripper towards the peg until it is slightly above the hole
    #  3. Align the peg with the hole
    #  4. Push the peg into the hole
    # First, we need to position the gripper to the side of the peg.
    if check("the robot's gripper is not positioned to the side of the peg"):
        robot.move_gripper("to the side of the peg")
    # Next, we move the gripper towards the peg until it is slightly above the hole.
    if check("the robot's gripper is not above the hole and is not aligned with the peg"):
        robot.move_gripper("above the hole", close_gripper=True)
    # We need to adjust the alignment of the peg with the hole before pushing it in.
    if check("the peg is not aligned with the hole"):
        robot.move_gripper("aligned with the hole")
    # Finally, we can push the peg into the hole.
    if check("the peg is aligned with the hole"):
        robot.move_gripper("pushing the peg into the hole")