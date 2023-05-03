# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. If gripper collides with wall, adjust gripper to avoid wall
    #  4. Slide puck to goal
    # This is like the push action, but we need to be careful not to collide with
    # the wall.
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.push("gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # loop over the next step until the puck is at the goal.
    while True:
        # Move the gripper and puck towards the goal.
        robot.slide("puck to goal")
        # If the gripper collides with the wall, move it over to avoid the wall.
        if check("gripper collides with wall"):
            robot.avoid("wall")