# Steps:
    #  1. Put gripper around the lever
    #  2. Rotate the gripper up
    # The first step is to put the gripper around the lever.
    if check("the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    # Once the gripper is around the lever, we can rotate it up to activate the
    # lever.
    if check("the robot's gripper is around lever and the lever is facing down"):
        robot.rotate("gripper up")