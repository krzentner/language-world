
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull the lever up
    # Put the gripper about above the lever.
    if check("the robot's gripper is not almost aligned with lever"):
        robot.put("gripper above lever")
    # If the lever is nearly aligned with the gripper, we can start to grab it by
    # moving the gripper around the lever.
    if check("the robot's gripper is almost aligned with lever and gripper is not around lever"):
        robot.drop("gripper around lever")
    # If the gripper is around the lever, start pulling up on it.
    if check("the robot's gripper is around lever"):
        robot.pull("lever up")