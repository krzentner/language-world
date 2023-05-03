# Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull mug towards target location
    #  4. Put mug down
    # First, put the gripper roughly above the mug handle, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the mug handle, put it around the handle.
    if check("the robot's gripper is not around the mug handle and the robot's gripper is open"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is near the mug handle and closed, we can grab it and move
    # it to the target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location", close_gripper=False)
    # If the gripper is near the target location, we can put the mug down.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location", close_gripper=True)