
    # Steps:
    #  1. Get the robot's gripper around the stick
    #  2. Pull the thermos toward the target location
    # First, put the robot's gripper around the stick.
    if check("the robot's gripper is not near the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    # Then we can pull the thermos toward the target location.
    if check("the robot's gripper is around the stick"):
        robot.move_gripper("toward the target location")