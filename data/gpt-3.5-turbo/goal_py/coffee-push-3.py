# Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around the mug handle
    #  3. Close gripper around the mug handle
    #  4. Move mug to the target location
    # First, we need to put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle", close_gripper=True)
    # Once the gripper is lined up above the mug handle, we should be able to
    # grab the handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.move_gripper("around the mug handle")
    # Once the gripper is around the mug handle, we can lift up the mug and move it to the target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location")