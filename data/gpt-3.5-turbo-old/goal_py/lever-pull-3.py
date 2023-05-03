    # Steps:
    #  1. Put gripper around the lever
    #  2. Rotate the lever up
    # To pull the lever, we need to position the gripper around it first.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we can rotate it by moving the
    # gripper upwards.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("above the lever")