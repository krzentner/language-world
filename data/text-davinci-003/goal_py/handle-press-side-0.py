
    # Steps:
    #  1. Put gripper to the side of the handle
    #  2. Push the handle
    # To side push the handle from the side, we need to put the gripper above the
    # handle and then move it to the side.
    # Move the gripper above the handle, so that it is roughly vertically
    # aligned with the handle.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # If the gripper is above the handle, move it to the side to push it.
    if check("the robot's gripper is almost vertically aligned with the handle"):
        robot.move_gripper("left of the handle")