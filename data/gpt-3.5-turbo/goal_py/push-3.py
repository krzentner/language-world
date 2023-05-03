# Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck to the target location
    # First, put the gripper near the puck so that we can push it.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # Once the gripper is near the puck, we can push it towards the target location.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("near the target location")