
    # Steps:
    #  1. Put gripper near stick
    #  2. Close gripper around stick
    #  3. Move thermos to goal, using stick as lever
    # First, we need to grab the stick by putting the gripper near it.
    if check("the robot's gripper is near the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    # If the gripper is above the stick and the gripper is open, close the
    # gripper to grab the stick.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("above the thermos")
    # If the gripper is at the end of the stick, hold the stick against the
    # thermos and push the thermos.
    if check("the robot's gripper is forward aligned with the thermos and the stick is not near the thermos"):
        robot.move_gripper("near the target location")