# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Slide the peg sideways out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg, slide the peg out of
    # the hole to the side.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("left of the peg", open_gripper=True)