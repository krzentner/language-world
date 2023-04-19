# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the hammer directly above the nail
    #  2. Lower the hammer onto the nail
    #  3. Pull the hammer up
    # The first step is to move the hammer so that it is directly above the nail.
    if check("the robot's gripper is not directly above the nail"):
        robot.move_gripper("directly above the nail")
    # Once the gripper is above the nail, we can lower the hammer onto the nail.
    if check("the robot's gripper is above the nail and the hammer is not touching the nail"):
        robot.move_gripper("touching the nail")
    # Finally, we need to pull the hammer back up.
    if check("the hammer is touching the nail"):
        robot.move_gripper("directly above the nail")