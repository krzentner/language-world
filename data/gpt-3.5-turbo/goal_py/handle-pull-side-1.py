# Steps:
    #  1. Put gripper next to handle
    #  2. Grab handle with gripper
    #  3. Pull up the handle
    # First, move the gripper next to the handle.
    if check("the robot's gripper is not next to the handle"):
        robot.move_gripper("next to the handle")
    # Once the gripper is next to the handle, we can grab it.
    if check("the robot's gripper is next to the handle and the gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Finally, we can pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")