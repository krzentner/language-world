# Steps:
    #  1. Put the gripper around the lever
    #  2. Pull the lever up
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we can just pull the lever up.
    if check("the robot's gripper is around the lever and the lever is pointing down"):
        robot.move_gripper("vertically aligned with the lever")