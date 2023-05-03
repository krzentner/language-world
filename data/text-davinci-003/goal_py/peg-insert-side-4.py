
    # Steps:
    #  1.Line up the gripper with the peg
    #  2.Grab the peg
    #  3.Pull the peg to the insertion hole
    #  4.Insert the peg into the hole
    # We don't know if the gripper is left or right of the peg, so we should try
    # to line up the gripper with the peg from a side view.
    # Start by moving the gripper near the peg from the side.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # If the gripper is in front of the peg, try to grab it.
    if check("the robot's gripper is forward aligned with the peg inserter and the robot's gripper is not closed"):
        robot.move_gripper("below the peg", close_gripper = True)
    # Once the robot has the peg, it can start to pull the peg towards the
    # insertion hole.
    if check("the robot's gripper is below the peg and the robot's gripper is closed"):
        robot.move_gripper("near the peg inserter")
    # When the peg is close to the insertion hole, line up the gripper according
    # to the direction of the hole and start pushing the peg in.
    if check("the robot's gripper is near the peg inserter"):
        robot.move_gripper("horizontally aligned with the peg inserter")