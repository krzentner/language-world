
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick by closing the gripper around it
    #  3. Move the stick in front of the thermos
    #  4. Push the thermos with the stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.move_gripper("vertically aligned with the stick")
    # If the stick is slightly left of the gripper, go back to putting the
    # gripper above the stick.
    if check("stick is not left of the robot's gripper and stick is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # As long as the gripper has control over the stick, move the stick in front
    # of the thermos.
    if check("the robot's gripper is ahead of the thermos"):
        robot.move_gripper("above the stick")
    # Now that the stick is in front of the thermos, we can push the thermos
    # with it.
    if check("the robot's gripper is forward aligned with the stick and the robot's gripper is not ahead of the thermos"):
        robot.move_gripper("near the target location")