
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Close gripper around mug handle
    #  4. Move mug to goal
    # First, put the gripper roughly above the mug handle, so that we don't bump
    # it while trying to grab it.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper isn't around the mug handle, put it around the mug handle.
    if check("the robot's gripper is not around mug handle and the robot's gripper is open"):
        robot.move_gripper("near the mug handle", close_gripper=True)
    # If the gripper is near the mug handle and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is above mug handle and the robot's gripper is closed"):
        robot.move_gripper("near the target location")