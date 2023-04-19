
    # Steps:
    #  1. Put gripper above lever
    #  2. Grab the lever with the gripper
    #  3. Rotate the lever up
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with the lever"):
        robot.move_gripper("vertically aligned with the lever", close_gripper=True)
    # If the lever is below the gripper, try to grab it.
    if check("the robot's gripper is vertically aligned with the lever and the lever is below the robot's gripper"):
        robot.move_gripper("above the lever")
    # Once the gripper is close enough, close the gripper around the lever and
    # rotate it up.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("horizontally aligned with the lever")