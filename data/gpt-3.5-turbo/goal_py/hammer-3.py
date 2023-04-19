# Steps:
    #  1. Put gripper above hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Lift hammer and move it above nail
    #  4. Swing hammer down onto nail
    # First, put the gripper above the hammer handle.
    if check("the robot's gripper is not above the hammer handle"):
        robot.move_gripper("above the hammer handle")
    # If the gripper isn't around the hammer handle, put it around the handle.
    if check("the robot's gripper is not around the hammer handle and the robot's gripper is open"):
        robot.move_gripper("near the hammer handle", close_gripper=True)
    # Once the gripper is around the handle, we can pick up the hammer.
    if check("the robot's gripper is around the hammer handle"):
        robot.move_gripper("above the nail")
    # Once the gripper is above the nail, we can swing the hammer down.
    if check("the robot's gripper is above the nail"):
        robot.move_gripper("above the hammer handle")  # lift the hammer back up
        robot.move_gripper("away from the nail")  # release the nail