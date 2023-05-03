# Steps:
    #  1. Put gripper near the peg
    #  2. Grab the peg
    #  3. Move gripper towards the hole
    #  4. Insert peg into the hole
    #  5. Release grip on peg
    # First, we need to move the gripper close to the peg.
    if check("the robot's gripper is not near the peg"):
        robot.move("gripper near the peg")
    # Once the gripper is near the peg, we can grab it.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.grab("the peg")
    # With the peg in the gripper, move it towards the hole.
    if check("the peg is in the gripper and the gripper is aligned with the hole"):
        robot.move("gripper towards the hole")
    # Once the gripper is aligned with the hole, insert the peg into the hole.
    if check("the gripper is aligned with the hole"):
        robot.insert("peg into the hole")
    # We inserted the peg into the hole, so we can release our grip on the peg.
    if check("the peg is inserted into the hole and the gripper is closed around it"):
        robot.release("grip on the peg")