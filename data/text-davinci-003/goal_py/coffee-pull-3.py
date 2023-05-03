
    # Steps:
    #  1. Put gripper around mug handle
    #  2. Pull mug towards target
    # First, put the gripper around the mug handle.
    if check("the robot's gripper is not around mug handle"):
        robot.move_gripper("around mug handle")
    # Now that the gripper is around the mug handle, as long as the mug isn't at
    # the target location we can start pulling the mug towards the target.
    if check("the robot's gripper is around the mug handle and the mug is not near the target location"):
        robot.move_gripper("left of the target location")