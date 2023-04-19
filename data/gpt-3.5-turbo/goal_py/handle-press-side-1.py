# Steps:
    #  1. Position gripper above the handle
    #  2. Move gripper around the handle
    #  3. Push down on the handle from the side
    # First, position the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is above the handle, move the gripper around the handle to
    # hold it.
    if check("the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Finally, push down on the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the handle")