
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull lever up
    # If the robot's gripper is not above the lever, we should move it above the
    # lever.
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # Once the gripper is above the lever, move it around the lever so that we
    # can grab the lever.
    if check("the robot's gripper is not around lever and the robot's gripper is open"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, pull it up.
    if check("the robot's gripper is around lever"):
        robot.move_gripper("up the lever")