
    # Steps:
    #  1. Move gripper to the target location
    # Move the gripper to the target location.
    if check("the robot's gripper is not above the target"):
        robot.move_gripper("above the target")