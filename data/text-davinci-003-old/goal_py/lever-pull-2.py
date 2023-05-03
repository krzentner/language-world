
    # Steps:
    #  1. Put gripper in front of the lever
    #  2. Pull the lever up
    # First, make sure the robot's gripper is roughly in front of the lever.
    if check("the robot's gripper is not forward aligned with lever"):
        robot.move_gripper("forward aligned with the lever")
    # Now that the gripper is in front of the lever, just pull it up.
    if check("the robot's gripper is forward aligned with the lever"):
        robot.move_gripper("above the lever", close_gripper=True)
    # If the gripper is above the lever, close the gripper and pull it up.
    if check("the robot's gripper is above the lever"):
        robot.move_gripper("up")