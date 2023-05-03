
    # Steps:
    #  1. Put gripper above hole
    #  2. Drop gripper around peg in hole
    #  3. Close gripper around peg
    #  4. Move peg to goal out of hole
    # First, put the gripper above the hole, not the peg itself.
    if check("the robot's gripper is not above the hole"):
        robot.move_gripper("above the hole")
    # We should be able to grab the peg by dropping the gripper around it
    # provided that the gripper is opened before doing this.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is closed around the peg, we can start moving the peg up
    # out of the hole.
    if check("the robot's gripper is around peg and peg is above the hole"):
        robot.move_gripper("vertically aligned with the target location")