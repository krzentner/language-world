
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal, with wall in the way
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Determine where the wall is in relation to the puck and the goal, and
    # move the puck (with the wall in the way) to the goal.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.navigate("puck and wall to goal")