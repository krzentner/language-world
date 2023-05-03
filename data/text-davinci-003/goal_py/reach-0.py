
    # Steps:
    #  1. Move gripper to target
    # If the gripper isn't at the target location, move it there.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")