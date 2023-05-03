
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop gripper around stick
    #  3. Close gripper around stick
    #  4. Pull thermos to goal using the stick
    # If the gripper isn't vertically above the stick, we should move the
    # gripper above it.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is above the stick, we can just drop it down to grab it.
    # We don't always need to close the gripper, since the stick is rigid and
    # won't take up space like a puck or thermos will.
    if check("the robot's gripper is near the stick"):
        robot.move_gripper("horizontally aligned with the thermos")
    # Once the robot is in front of the thermos, the robot just needs to pull
    # the stick back towards the target location to move it.
    if check("the robot's gripper is horizontally aligned with the thermos"):
        robot.move_gripper("near the target location")