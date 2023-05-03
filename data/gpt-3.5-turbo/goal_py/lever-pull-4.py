# Steps:
    #  1. Put the gripper above the lever handle
    #  2. Grab the lever handle
    #  3. Push or pull the lever to rotate it up
    # First, put the gripper above the lever handle.
    if check("the robot's gripper is not above the lever handle"):
        robot.move_gripper("above the lever handle")
    # Once the gripper is above the lever handle, we should be able to grab it
    # by moving the gripper down around it.
    if check("the robot's gripper is above the lever handle and the robot's gripper is not around the lever handle"):
        robot.move_gripper("around the lever handle")
    # Once the gripper is around the lever handle, we can push or pull the lever
    # to rotate it up.
    if check("the robot's gripper is around the lever handle"):
        robot.move_gripper("rotate the lever up")