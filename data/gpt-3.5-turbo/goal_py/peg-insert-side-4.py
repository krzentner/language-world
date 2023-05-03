# Steps:
    # 1. Put gripper next to peg
    # 2. Grab the peg
    # 3. Insert the peg into the hole
    # First, put the gripper next to the peg.
    if check("the robot's gripper is not next to the peg"):
        robot.move_gripper("next to the peg")
    # Once the gripper is next to the peg, we can grab it by closing the gripper.
    if check("the robot's gripper is next to the peg and the gripper is not closed"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Once the gripper is around the peg, we can insert the peg into the hole.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("into the hole")