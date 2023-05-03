# Steps:
    #  1. Put gripper near peg
    #  2. Pick up the peg with gripper
    #  3. Move gripper to hole
    #  4. Insert the peg into the hole from the side
    # First, put the gripper near the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # If the gripper is near the peg, try to pick it up by closing the gripper around it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper has the peg, move it to the hole.
    if check("the peg is in the robot's gripper and the robot's gripper is not near the hole"):
        robot.move_gripper("near the hole")
    # Finally, insert the peg into the hole from the side.
    if check("the robot's gripper is near the hole"):
        robot.move_gripper("horizontally aligned with the hole")