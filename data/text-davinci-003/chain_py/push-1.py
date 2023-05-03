
    # Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck towards the target
    # We don't have a way to grab the puck, so put the robot's gripper near the
    # puck instead.
    if check("the robot's gripper is not near the puck"):
        robot.put("gripper near puck")
    # If the puck is near the goal, just push it towards the goal, and if the
    # puck is near the gripper, just push it towards the goal.
    if check("the puck is near gripper or the puck is near goal"):
        robot.push("puck towards goal")