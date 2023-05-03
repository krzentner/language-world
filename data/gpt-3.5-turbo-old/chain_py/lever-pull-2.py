    # Steps:
    #  1. Put gripper around lever
    #  2. Pull gripper upwards to rotate the lever
    #  3. Release the lever
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.grab("lever")
    # If the gripper is around the lever, we can pull upwards to rotate the
    # lever.
    if check("the robot's gripper is around the lever"):
        robot.pull("gripper upwards")
    # Once we've rotated the lever, we need to release it so that it falls back
    # down.
    if check("the lever is rotated upwards"):
        robot.release("lever")