
    # Steps:
    #  1. Put gripper below lever
    #  2. Push lever up
    # First, line the robot's gripper up with the lever from below.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.move_gripper("vertically aligned with the lever")
    # Once the gripper is aligned with the lever, we can just push it up.
    if check("the robot's gripper is vertically aligned with lever"):
        robot.move_gripper("above the lever")