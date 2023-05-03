# Steps:
    #  1. Put gripper right of the peg
    #  2. Grab the peg with the gripper
    #  3. Pull the peg out from the side
    # First, put the gripper right of the peg.
    if check("the robot's gripper is not right of the peg"):
        robot.move_gripper("right of the peg")
    # If the gripper is not around the peg, grab the peg with the gripper.
    if check("the robot's gripper is not around the peg" and "the robot's gripper is open"):
        robot.move_gripper("around the peg")
    # Once the gripper is around the peg, pull the gripper and the peg out to
    # the side.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("to the side")