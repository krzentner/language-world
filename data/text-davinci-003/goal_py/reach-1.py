
    # Steps:
    #  1. Move gripper to the target location
    # If the robot's gripper is not near the target location, move the gripper
    # towards the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")