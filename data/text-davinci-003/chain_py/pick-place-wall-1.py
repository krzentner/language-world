
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move puck up and over the wall
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by
    # closing the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Move the puck up and over the wall.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.pickup("puck up and over wall")
    # If the puck is over the wall, just move it to the goal.
    if check("the puck is over the wall"):
        robot.place("puck at goal")