# Steps:
    #  1. Put gripper around lever
    #  2. Pull the lever up
    # First, put the gripper around the lever, since it's a small object that we
    # need to grab.
    if check("the robot's gripper is not around lever"):
        robot.grab("lever")
    # Once the gripper is around the lever, we can just pull it up.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")