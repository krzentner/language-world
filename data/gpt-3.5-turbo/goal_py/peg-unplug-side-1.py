# Steps:
    #  1. Put gripper around the peg
    #  2. Pull the peg out to the side
    # First, put the gripper around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Once the gripper is around the peg, we can pull it out to the side.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("beside the peg")