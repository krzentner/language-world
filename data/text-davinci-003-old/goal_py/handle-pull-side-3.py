
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Pull up the handle
    # First, put the gripper left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # If the gripper is left of the handle and the gripper isn't near the handle,
    # move the gripper near the handle.
    if check("the robot's gripper is left of the handle and the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once the gripper is near the handle, pull up on the handle.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("above the handle")