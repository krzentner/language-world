# Steps:
    #  1. Put gripper around the lever
    #  2. Pull up on the lever
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we can pull up on the lever to
    # rotate it up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("vertically aligned with the lever")