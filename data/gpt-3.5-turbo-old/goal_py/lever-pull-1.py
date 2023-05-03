# Steps:
    #  1. Put gripper around the lever
    #  2. Pull the lever up
    # First, position gripper around the lever.
    if check("the robot's gripper is not around the lever and the gripper is open"):
        robot.move_gripper("near the lever", close_gripper=True)
    # Once gripper is around the lever, pull the lever up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("above the lever")