
    # Steps:
    #  1. Put gripper left of the peg
    #  2. Grab the peg with the gripper
    #  3. Slide the peg sideways out of the hole
    # First, put the gripper left of the peg.
    if check("the robot's gripper is not left of the peg and the robot's gripper is not vertically aligned with peg"):
        robot.move_gripper("vertically aligned with the peg", close_gripper=True)
    # If the peg became in front of the gripper, go back around the peg.
    if check("peg is not left of the robot's gripper"):
        robot.move_gripper("left of the peg")
    # As long the gripper is still mostly around the peg, plug it out.
    if check("the robot's gripper is left of the peg and the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")