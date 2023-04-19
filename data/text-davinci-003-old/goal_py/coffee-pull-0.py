
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab the mug with the gripper
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.move_gripper("vertically aligned with the mug")
    # If the mug is not below the gripper, move the gripper closer to the mug.
    if check("the robot's gripper is not near mug"):
        robot.move_gripper("near the mug", close_gripper=True)
    # If the gripper is close to the mug, we probably have it in our grip.
    # Pull the mug towards the target location.
    if check("the robot's gripper is near the mug and the mug is below the robot's gripper"):
        robot.move_gripper("above the target location")