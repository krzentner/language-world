# Steps:
    # 1. Put gripper above the peg
    # 2. Apply force on the peg to loosen it
    # 3. Slide the gripper around the peg
    # 4. Carefully pull the gripper and the peg out of the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the gripper isn't around the peg, put it around the peg and apply
    # force to loosen it.
    if check("the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg")
    # Slide the gripper around the peg.
    if check("the robot's gripper is around the peg and not horizontally aligned with the peg's hole"):
        robot.move_gripper("horizontally aligned with the peg's hole")
    # If the gripper is horizontally aligned with the hole, carefully pull the
    # gripper and the peg out.
    if check("the robot's gripper is around the peg and is horizontally aligned with the peg's hole"):
        robot.move_gripper("above the peg and hole")