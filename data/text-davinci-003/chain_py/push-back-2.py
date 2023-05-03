
    # Steps:
    #  1. Put gripper behind puck
    #  2. Push gripper behind puck
    #  3. Slide puck towards goal
    # To move a puck backwards, the robot should move the gripper around to the
    # behind the puck.
    # If the robot's gripper is not behind the puck and near it, move it to be
    # behind the puck.
    if check("the robot's gripper is not behind puck"):
        robot.push("gripper to behind puck")
    # If the gripper is behind the puck and near it, just push the puck backwards.
    if check("the robot's gripper is behind the puck"):
        robot.slide("puck towards goal")