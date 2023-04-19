# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up on the handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # If the gripper is around the handle, pull up on the handle.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above the handle")