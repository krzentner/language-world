# Steps:
    #  1. Move gripper above target location
    #  2. Lower gripper to reach target location
    # First, position the gripper above the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Then, lower the gripper to reach the target location.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("near the target location")