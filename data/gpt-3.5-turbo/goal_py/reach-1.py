# Steps:
    #  1. Move gripper to target location
    # First, move the gripper to the target location while keeping it open.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")