
    # Steps:
    #  1. Put gripper near puck
    #  2. Push puck to goal
    # First, put the gripper near the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck")
    # If the gripper is near the puck, we can just push the puck towards the
    # target location.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("near the target location")