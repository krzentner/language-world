# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Open the gripper around the stick
    #  3. Move the gripper to the thermos
    #  4. Close the gripper around the thermos
    #  5. Move the thermos to the target location using the stick to pull it
    # First, put the gripper roughly above the stick so that we can grab it.
    if check("the gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the gripper is not around the stick and the gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick, move the gripper to the thermos.
    if check("the gripper is around the stick and the gripper is not above the thermos"):
        robot.move_gripper("above the thermos")
    # If the gripper is above the thermos, close the gripper to grab the thermos.
    if check("the gripper is above the thermos and the gripper is open"):
        robot.move_gripper("above the thermos", close_gripper=True)
    # If the gripper is holding the thermos, move the thermos to the target
    # location using the stick to pull it.
    if check("the gripper is holding the thermos and the thermos is not at the target location"):
        robot.move_gripper("near the target location", stick=True)