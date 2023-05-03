
    # Steps:
    #  1. Put gripper around the stick
    #  2. Pull the thermos towards the target location
    # If the stick isn't near the gripper, line it up with the gripper from the
    # front.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("forward aligned with the stick")
    # If the stick is near the gripper, we can try to grab it by closing the
    # gripper around it.
    if check("the robot's gripper is near the stick and the robot's gripper is not closed"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # If the gripper is closed, just pull the thermos.
    if check("the robot's gripper is closed and stick is near the robot's gripper"):
        robot.move_gripper("near the target location")