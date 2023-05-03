# Steps:
    #  1. Put gripper on the lever
    #  2. Rotate the lever up
    # To start, put the gripper over the lever.
    if check("the robot's gripper is not on the lever"):
        robot.move("gripper to lever")
    # Once the gripper is on the lever, rotate it up.
    if check("the robot's gripper is on the lever"):
        robot.rotate("lever up")