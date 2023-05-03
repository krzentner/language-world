# Steps:
    # 1. Move gripper above target location
    # 2. Move gripper down to target location without touching anything
    # We just need to move the gripper to the target location without touching
    # anything on the way.
    if check("the robot's gripper is not above the target location and the robot's gripper is not aligned with the target location"):
        robot.move_gripper("above the target location")
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("at the target location")