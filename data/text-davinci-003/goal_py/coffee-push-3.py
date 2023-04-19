
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Move mug to target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # If the gripper isn't around the mug handle, move it around the mug handle.
    if check("the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Once the gripper is around the mug handle, move the mug to the target
    # location.
    if check("the robot's gripper is around mug handle"):
        robot.move_gripper("near the target location")