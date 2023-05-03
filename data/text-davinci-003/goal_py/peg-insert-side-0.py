
    # Steps:
    #  1. Put gripper near peg
    #  2. Pick up peg
    #  3. Move into hole
    #  4. Push into hole
    # We want to grab the peg from the side, so first put the gripper near the 
    # peg.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is open and the robot's gripper is vertical aligned with peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is not in the hole, move it into the hole.
    if check("the robot's gripper is around peg and the robot's gripper is outside the hole"):
        robot.move_gripper("into the hole")
    # If the gripper is inside the hole, just push it in to insert the peg.
    if check("the robot's gripper is inside hole"):
        robot.move_gripper("into the hole")