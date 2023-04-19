
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Sweep cube to target location
    # First, place the gripper above the cube.
    if check("the robot's gripper is not above cube"):
        robot.move_gripper("above the cube")
    # If the gripper is above the cube but not around it, we can line it up by
    # moving the gripper around it.
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.move_gripper("around the cube", close_gripper=True)
    # Now that the gripper is around the cube, we can sweep it towards the
    # target location.
    if check("the robot's gripper is around cube"):
        robot.move_gripper("near the target location")