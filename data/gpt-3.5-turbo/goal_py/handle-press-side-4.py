# Steps:
    #  1. Put gripper to the right of the handle
    #  2. Lower the gripper onto the handle
    #  3. Push the handle down
    # First, put the gripper to the right of the handle.
    if check("the robot's gripper is not right of the handle"):
        robot.move_gripper("right of the handle")
    # Once the gripper is to the right of the handle, we can lower it onto the handle.
    if check("the robot's gripper is right of the handle and the robot's gripper is not low enough to touch handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # Once the gripper is lowered onto the handle, we can push the handle down by moving the gripper sideways.
    if check("the robot's gripper is touching the handle"):
        robot.move_gripper("horizontally aligned with the handle")