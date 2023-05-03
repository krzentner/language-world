
    # Steps:
    #  1. Line up the gripper behind the puck
    #  2. Push the puck towards the goal
    # First, line up the robot's gripper with the puck from behind.
    if check("the robot's gripper is not behind the puck"):
        robot.place("gripper behind puck")
    # Now that the gripper is lined up, just push the puck towards the goal.
    if check("the robot's gripper is behind the puck"):
        robot.penetrate("puck forward")