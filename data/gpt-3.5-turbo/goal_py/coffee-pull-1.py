# Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Pull mug to target location
    # First, put the gripper roughly above the mug handle, so we don't knock it
    # over.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the mug handle, put it around the mug handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, we can probably pull the mug to
    # the target location now.
    # We should close the gripper to make sure we keep a good grip on the mug.
    if check("the robot's gripper is around the mug handle and the robot's gripper is closed"):
        robot.move_gripper("above the target location")