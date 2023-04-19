
    # Steps:
    #  1. Put gripper above puck and near the wall
    #  2. Move gripper against the wall while dropping around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # If the gripper isn't near the wall, move it there.
    if check("the robot's gripper is not near the wall and the robot's gripper is not above puck"):
        robot.put("gripper above puck and near the wall")
    # If the gripper is near the wall and below the puck, move it against the
    # wall while dropping it around the puck.
    if check("the robot's gripper is near the wall and below the puck"):
        robot.move("gripper against wall while dropping around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")