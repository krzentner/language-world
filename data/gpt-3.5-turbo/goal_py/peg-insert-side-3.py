# Steps:
    #  1. Put gripper slightly above peg, to the side of the hole
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move gripper towards the hole
    #  5. Insert the peg into the hole
    #  6. Release the peg
    # First, put the gripper slightly above the peg to the side of the hole.
    if check("the robot's gripper is not above the peg and to the side of the hole"):
        robot.move_gripper("above the peg and to the side of the hole")
    # Drop the gripper around the peg and close it to grab the peg.
    if check("the robot's gripper is above the peg and the gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Move the gripper towards the hole while keeping it slightly above the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("above the hole")
    # Insert the peg into the hole by lowering the gripper and pushing the peg in.
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("in the hole", close_gripper=True)
    # Release the peg by opening the gripper.
    if check("the gripper is holding the peg"):
        robot.move_gripper("above the peg", close_gripper=False)