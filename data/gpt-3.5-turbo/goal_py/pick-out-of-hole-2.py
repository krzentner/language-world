# Steps:
    #  1. Put the gripper above the peg
    #  2. Drop the gripper around the peg
    #  3. Lift the peg out of the hole
    #  4. Move the gripper to the target location
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper is above the peg but not around it, put it around the peg.
    if check("the robot's gripper is above the peg and the robot's gripper is not closed around the peg"):
        robot.move_gripper("near the peg", close_gripper=True)
    # Once the gripper is around the peg, lift it out of the hole by moving the
    # gripper upward.
    if check("the robot's gripper is around the peg and the robot's gripper is not near the target location"):
        robot.move_gripper("above the target location")