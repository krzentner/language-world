# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift puck over wall to target location
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move("gripper to above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the gripper is not around puck"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the gripper is near the puck and the gripper is open"):
        robot.grab("puck")
    # The puck is now held by the gripper.
    # Check if we need to lift it over the wall to get it to the goal.
    if check("the gripper is holding the puck and the puck is below or at the height of the wall"):
        robot.lift("puck over the wall")
    # We lifted the puck over the wall, and it's still held by the gripper.
    # Move the puck to the goal.
    if check("the gripper is holding the puck and the puck is above the height of the wall"):
        robot.move("puck to goal")