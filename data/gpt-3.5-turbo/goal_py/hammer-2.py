# Steps:
    #  1. Put gripper above hammer handle
    #  2. Grab the hammer handle with the gripper
    #  3. Raise and position the hammer over the nail
    #  4. Swing the hammer and hit the nail
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not above the hammer handle"):
        robot.move_gripper("above the hammer handle")
    # If the gripper is not around the hammer handle, move it close and grab the
    # handle.
    if check("the robot's gripper is not around the hammer handle and the robot's gripper is open"):
        robot.move_gripper("near the hammer handle", close_gripper=True)
    # If the gripper is now around the hammer handle, move the hammer over the
    # nail.
    if check("the robot's gripper is around the hammer handle and the robot's gripper is not over the nail"):
        robot.move_gripper("over the nail")
    # Once the hammer is over the nail, swing it to hit the nail.
    if check("the robot's gripper is over the nail"):
        robot.swing_hammer()