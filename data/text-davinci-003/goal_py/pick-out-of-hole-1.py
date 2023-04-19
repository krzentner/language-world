
    # Steps:
    #  1. Put gripper almost directly above the peg
    #  2. Drop gripper down around the peg 
    #  3. Close gripper around peg 
    #  4. Move peg to goal 
    # First, put the gripper roughly above the peg, so that we don't miss it
    # while trying to grab it
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg, we should be able to grab it by closing
    # the gripper.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.move_gripper("near the target location")