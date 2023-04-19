# Steps:
    #  1. Put gripper around lever
    #  2. Rotate the gripper to pull up the lever
    # First, put the gripper around the lever.
    if check("the robot's gripper is not around the lever"):
        robot.drop("gripper around lever")
    # If the gripper is around the lever, try to rotate it up.
    if check("the robot's gripper is around lever"):
        robot.rotate("gripper up to pull lever")