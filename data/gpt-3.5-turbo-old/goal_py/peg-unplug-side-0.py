# Steps:
    #  1. Put gripper above the top of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out horizontally from the hole
    # First, put the gripper above the top of the peg.
    if check("the robot's gripper is not vertically aligned with the top of the peg"):
        robot.move_gripper("vertically aligned with the top of the peg")
    # If the gripper is not around the peg, move it to grip it.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # As long as the gripper is still around the peg, pull it out horizontally.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("left of the peg")