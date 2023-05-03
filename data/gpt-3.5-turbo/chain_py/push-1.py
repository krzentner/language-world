# Steps:
    #  1. Put gripper roughly above puck
    #  2. Drop gripper around puck
    #  3. Push puck to goal
    # First, put the gripper roughly above the puck, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # Once the gripper is around the puck, push the puck towards the goal.
    if check("the robot's gripper is around puck"):
        robot.push("puck towards goal")