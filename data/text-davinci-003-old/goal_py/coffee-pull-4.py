
    # Steps:
    #  1. Put gripper to the left of the mug
    #  2. Grab the mug with the gripper
    #  3. Pull the mug to the target location
    # We just need to align the robot's gripper with the mug to be able to grab
    # it.
    if check("the robot's gripper is not horizontally aligned with the mug"):
        robot.move_gripper("horizontally aligned with the mug", close_gripper=True)
    # The mug should now be held in the robot's gripper. The robot can now just
    # pull the mug by moving the top of the gripper to the target location.
    if check("the robot's gripper is horizontally aligned with the mug"):
        robot.move_gripper("above the target location")