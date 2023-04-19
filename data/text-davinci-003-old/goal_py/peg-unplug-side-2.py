
    # Steps:
    #  1. Put gripper around the peg
    #  2. Pull the peg sideways to unplug it
    # First, put the gripper around the peg to grab hold of it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # If the gripper is around the peg, we can pull the peg sideways to unplug
    # it.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("right of the peg")