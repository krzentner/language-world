
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move the puck up and over the wall
    #  5. Place the puck at the goal
    # First, put the gripper above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
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
    # Try to move the puck up and over the wall.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.lift("puck up and over wall")
    # If we got the puck up and over the wall, move it to the goal.
    if check("the puck is on the other side of the wall"):
        robot.place("puck at goal")