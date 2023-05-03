# Steps:
    #  1. Put gripper around the puck
    #  2. Push the puck towards the target location
    # First, we need to put the gripper around the puck, so that we can push it.
    if check("the robot's gripper is not around the puck"):
        robot.drop("gripper around puck")
    # Once the gripper is around the puck, we can push it towards the target
    # location.
    if check("the robot's gripper is around the puck and the puck is not at the goal"):
        robot.push("puck towards goal")