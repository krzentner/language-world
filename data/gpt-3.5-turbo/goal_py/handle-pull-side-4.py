# Steps:
    #  1. Put gripper around the handle from the side
    #  2. Pull up on the handle
    # Since we're pulling the handle from the side, we need to put the gripper
    # around it from the side.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle", close_gripper=True)
    # Once the gripper is around the handle from the side, we can pull up on it.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")