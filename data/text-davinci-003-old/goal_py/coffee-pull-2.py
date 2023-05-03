
    # Steps:
    #  1. Put gripper above the mug
    #  2. Close gripper around the mug
    #  3. Pull the mug towards the target
    # First, line up gripper with the mug from above.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.move_gripper("vertically aligned with the mug")
    # Now that the gripper is above the mug, close it to trap the mug.
    if check("the robot's gripper is not around mug"):
        robot.move_gripper("above the mug", close_gripper=True)
    # If the gripper is around the mug and near the goal, we can pull the mug
    # towards the target.
    if check("the robot's gripper is around mug and near the goal"):
        robot.move_gripper("towards the target")