
    # Steps:
    #  1. Put gripper horizontally above the peg
    #  2. Drop gripper into the hole
    #  3. Close gripper around peg
    #  4. Move peg to goal
    # Because of the hole, the robot can't just move the gripper around the peg.
    # It has to first move the gripper above the peg, and then lower the gripper
    # into the hole, trapping the peg.
    # First, line up the gripper with the peg from the front.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg")
    # Now, lower the gripper into the hole to trap the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not in the hole"):
        robot.move_gripper("above the peg", close_gripper=True)
    # If the gripper is in the hole and open, maybe we can grab the peg by
    # closing the gripper.
    if check("the robot's gripper is in the hole and the robot's gripper is closed"):
        robot.move_gripper("near the target location")