
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck around wall
    #  4. Slide puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # If the wall is close enough we can slide the puck around it by pushing it
    # with the gripper
    if check("the puck is near wall and the robot's gripper is closed"):
        robot.slide("the puck around wall")
    # If the wall is no longer in the way, we can just push the puck to the goal.
    if check("the wall is not in the way of the puck"):
        robot.slide("the puck to goal")