
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around the lever
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever", close_gripper=True)
    # As long as the gripper is don't closed all the way around the lever,
    # rotate the lever.
    if check("the robot's gripper is vertically aligned with the lever and the lever is not rotated up"):
        robot.move_gripper("up around the lever")
    # If the lever is already rotated up, just keep the gripper closed on it
    # for now.
    if check("the lever is rotated up"):
        robot.move_gripper("above the lever")