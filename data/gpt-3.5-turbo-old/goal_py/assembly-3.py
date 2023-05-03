# Steps:
    #  1. Put gripper above the wrench and peg
    #  2. Position the gripper such that it can grab the wrench
    #  3. Grab the wrench
    #  4. Position the gripper above the peg
    #  5. Move the gripper down to place the wrench around the peg
    #  6. Open the gripper to release the wrench
    # First, put the gripper roughly above the wrench and peg.
    if check("the robot's gripper is not above the wrench and peg"):
        robot.move_gripper("above the wrench and peg")
    # If the gripper is not around the wrench but roughly lined up with it,
    # close the gripper.
    if check("the robot's gripper is not around the wrench and the gripper is roughly lined up with the wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # If the gripper has the wrench and is not above the peg, move the gripper
    # above the peg horizontally.
    if check("the robot's gripper has the wrench but is not horizontally aligned with the peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # If the gripper has the wrench and is above the peg horizontally, move
    # the gripper down to the peg and open the gripper to release the wrench.
    if check("the robot's gripper is horizontally aligned with the peg and the gripper is not near the peg"):
        robot.move_gripper("around the peg", open_gripper=True)