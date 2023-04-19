# Steps:
    #  1. Put gripper around the lever
    #  2. Pull the gripper up to rotate the lever
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, pull up to rotate the lever.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("vertically aligned with the lever")