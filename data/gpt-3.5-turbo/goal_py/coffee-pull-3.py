# Steps:
    #  1. Put gripper around the mug handle
    #  2. Lift the mug to get it off the table
    #  3. Pull the mug to the target location
    # First, put the gripper around the mug handle.
    if check("the robot's gripper is not around the mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)
    # Lift the mug to get it off the table.
    if check("the robot's gripper is around the mug handle and the robot's gripper is not lifted"):
        robot.move_gripper("lifted")
    # Pull the mug to the target location.
    if check("the robot's gripper is lifted and not above the target location"):
        robot.move_gripper("above the target location")