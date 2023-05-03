# Steps:
    #  1. Put the gripper above the stick
    #  2. Drop the gripper around the stick
    #  3. Grab the stick by closing the gripper
    #  4. Move the stick to the thermos
    #  5. Put the gripper to the thermos
    #  6. Grab the thermos by closing the gripper around it
    #  7. Move the thermos to the target location by pulling it with the stick
    # First, put the gripper roughly above the stick so that we don't bump it.
    if check("the gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # Once the gripper is above the stick, move it down and grab the stick by
    # closing the gripper around it.
    if check("the gripper is above the stick and the gripper is not around the stick"):
        robot.move_gripper("around the stick", close_gripper=True)
    # Once the stick is in the gripper, move it to the thermos.
    if check("the gripper is around the stick and the gripper is not near the thermos"):
        robot.move_gripper("near the thermos")
    # Put the gripper around the thermos.
    if check("the gripper is near the thermos and the gripper is not around the thermos"):
        robot.move_gripper("around the thermos", close_gripper=True)
    # Move the thermos to the target location by pulling it with the stick.
    if check("the gripper is around the thermos and the thermos is not at the target location"):
        # Push the stick against the ground to pull the thermos.
        robot.move_gripper("against the ground")
        # Slide the stick handle to "pull" the thermos.
        robot.move_gripper("horizontally aligned with the thermos", close_gripper=True)
        robot.move_gripper("near the target location")