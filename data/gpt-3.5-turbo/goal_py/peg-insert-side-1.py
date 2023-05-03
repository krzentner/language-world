# Steps:
    #  1. Put the gripper above the peg
    #  2. Drop the gripper around the peg
    #  3. Close the gripper around the peg
    #  4. Move the gripper to the side of the hole
    #  5. Rotate the gripper to align the peg with the hole
    #  6. Insert the peg into the hole
    # First, put the gripper above the peg, so that we can grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Move the gripper to the side of the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("to the side of the hole")
    # Rotate the gripper so that the peg is aligned with the hole.
    if check("the robot's gripper is to the side of the hole"):
        robot.rotate_gripper("aligned with the hole")
    # Insert the peg into the hole.
    if check("the robot's gripper is aligned with the hole"):
        robot.move_gripper("inside the hole")