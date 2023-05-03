# Steps:
    #  1. Put gripper above lever
    #  2. Grab onto lever
    #  3. Rotate the lever up
    # First, we need to position the gripper above the lever.
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # Once the gripper is positioned above the lever, we can grab onto it by
    # moving the gripper down around it.
    if check("the robot's gripper is above the lever and the robot's gripper is not around the lever"):
        robot.move_gripper("around the lever", close_gripper=True)
    # Once the gripper is around the lever, we can pull up on it to rotate it
    # up.
    if check("the robot's gripper is around the lever and the lever is not in the up position"):
        robot.move_gripper("above the lever")