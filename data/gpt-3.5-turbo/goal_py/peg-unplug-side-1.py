# Steps:
    #  1. Put gripper around the peg
    #  2. Move the gripper to the side of the peg
    #  3. Pull the peg out of the hole
    # First, put the gripper around the peg.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # Once the gripper is around the peg, move it to the side of the peg so that
    # we can pull the peg out of the hole.
    if check("the robot's gripper is around the peg and is not left of the peg"):
        robot.move_gripper("left of the peg")
    # Finally, pull the peg out of the hole.
    if check("the robot's gripper is left of the peg"):
        robot.move_gripper("far from the peg")