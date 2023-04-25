
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Drop gripper around the mug handle
    #  3. Pull the mug to the target location
    # First, put the gripper from above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle")
    # If the gripper is not around the mug handle, drop it around the mug
    # handle.
    if check("the robot's gripper is not around the mug handle"):
        robot.move_gripper("around the mug handle")
    # Finally, pull the mug to the target location.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("near the target location")