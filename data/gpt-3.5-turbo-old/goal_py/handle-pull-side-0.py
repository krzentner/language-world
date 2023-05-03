# Steps:
    #  1. Align gripper left of the handle
    #  2. Use gripper to pull up the handle from the side
    # First, put the gripper left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # Once the gripper is left of the handle, we can use it to pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")