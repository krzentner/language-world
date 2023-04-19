
    # Steps:
    #  1. Line up the gripper with the peg from the side
    #  2. Push the peg out of the hole
    # First, we need to line up the robot's gripper with the peg from the side.
    if check("the robot's gripper is not horizontally aligned with peg"):
        robot.move_gripper("horizontally aligned with the peg")
    # Once the gripper is lined up, push against the peg from the side to push
    # it out of the hole.
    if check("the robot's gripper is horizontally aligned with peg"):
        robot.move_gripper("above the peg")