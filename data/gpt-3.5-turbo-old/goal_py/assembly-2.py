# Steps:
    #  1. Put gripper above wrench and peg
    #  2. Position the gripper around the wrench and the peg
    #  3. Tighten the wrench around the peg by rotating the gripper
    # First, put the gripper above the wrench and the peg
    if check("the robot's gripper is not above the wrench and peg"):
        robot.move_gripper("above the wrench and peg")
    # If the gripper isn't around the wrench and peg, position it there.
    if check("the robot's gripper is not around the wrench and peg"):
        robot.move_gripper("around the wrench and peg")
    # If the gripper is around the wrench and peg, tighten the wrench by rotating
    # the gripper.
    if check("the robot's gripper is around the wrench and peg"):
        robot.rotate_gripper("tighten")