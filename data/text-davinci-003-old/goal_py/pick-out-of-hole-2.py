
    # Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper around the peg
    #  3. Pull the peg out of the hole
    #  4. Move peg to the target location
    # First, put the gripper above the hole, so that we don't bump the peg while
    # trying to grab it.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the peg is not below the robot's gripper and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing
    # the gripper.
    if check("the peg is below the robot's gripper and the robot's gripper is closed"):
        robot.move_gripper("above the target location")