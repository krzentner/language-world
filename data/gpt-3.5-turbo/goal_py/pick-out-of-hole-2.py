# Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Move the peg out of the hole
    #  4. Move the peg to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg, lift the peg out of
    # the hole.
    if check("peg is not above the hole"):
        robot.move_gripper("above the hole")
    # If the peg is above the hold, move it to the target location.
    if check("the robot's gripper is around peg"):
        robot.move_gripper("near the target location")