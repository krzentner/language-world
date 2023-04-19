# Steps:
    #  1. Put gripper around the lever
    #  2. Pull the lever up
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.drop("gripper around lever")
    # Once the gripper is around the lever, we can just pull it up.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")