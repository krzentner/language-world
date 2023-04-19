
    # Steps:
    #  1. Move the claw to the peg
    #  2. Open the claw and put it around the peg
    #  3. Close the claw so that it grips the peg
    # First, move the gripper to the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move_gripper("near the peg")
    # If the gripper is near the peg but not around it, open it and put it
    # around the peg.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is closed, we must have successfully put the claw around the
    # peg. Now we can close the gripper to make sure it holds onto the peg.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("above the peg")