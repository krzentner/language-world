
    # Steps:
    #  1. Put gripper directly above the hole
    #  2. Drop gripper around the peg
    #  3. Close gripper around the peg
    #  4. Lift the peg out of the hole
    # First, put the gripper directly above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # Once the gripper is above the peg, drop the gripper around the peg and
    # close the gripper.
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is closed around the peg and it is still in the hole,
    # lift the peg up out of the hole.
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.move_gripper("above the target location")