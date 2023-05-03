
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull lever upwards
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever")
    # If the gripper is vertically aligned, drop it around the lever. This is
    # easier since the angle of the gripper is fixed so we don't have to be
    # careful of the direction.
    if check("the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever")
    # Once the gripper is around the lever, we can just pull the lever up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("vertically aligned with the lever")