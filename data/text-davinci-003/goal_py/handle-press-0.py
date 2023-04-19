
    # Steps:
    #  1. Put the gripper almost vertically aligned with the handle
    #  2. Push down on the handle until it clicks
    # Place the gripper above the handle.
    if check("the robot's gripper is not almost vertically aligned with the handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # Once the gripper is aligned with the handle, we need to push firmly down to
    # click it.
    if check("the robot's gripper is almost vertically aligned with the handle"):
        robot.move_gripper("below the handle")
    # If the handle is almost clicked, push harder until it clicks.
    if check("the robot's gripper is below the handle"):
        robot.move_gripper("horizontally aligned with the handle")