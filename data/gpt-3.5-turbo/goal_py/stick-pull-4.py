# Steps:
    #  1. Put gripper below stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos
    #  4. Pull the thermos to the target location using the stick
    # We first need to put the gripper below the stick.
    if check("the robot's gripper is not below the stick"):
        robot.move_gripper("below the stick")
    # Once the gripper is below the stick, we can close the gripper around it.
    if check("the robot's gripper is below the stick and the robot's gripper is not around the stick"):
        robot.move_gripper("around the stick")
    # With the stick in the gripper, we can line it up with the thermos.
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with the thermos"):
        robot.move_gripper("horizontally aligned with the thermos")
    # Once the stick is lined up with the thermos, we can pull the thermos to the
    # target location using the stick.
    if check("the robot's gripper is around the stick and the stick is horizontally aligned with the thermos"):
        robot.move_gripper("near the target location")