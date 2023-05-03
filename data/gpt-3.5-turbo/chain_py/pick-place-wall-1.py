# Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to just above the wall
    #  5. Move the gripper to the other side of the wall
    #  6. Lower the puck to the other side of the wall
    #  7. Open the gripper to release the puck
    # First, put the gripper roughly above the puck, but make sure it's high
    # enough to clear the wall.
    if check("the robot's gripper is not above the puck and the puck is below the wall height"):
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
    # Move the puck just above the wall.
    if check("the robot's gripper is above puck and the puck is above the wall height and the puck is not right above the wall"):
        robot.place("puck just above the wall")
    # Move the gripper to the other side of the wall.
    if check("the robot's gripper is just above the wall and the gripper is not on the other side yet"):
        robot.move("gripper to the other side of the wall")
    # Lower the puck to the other side of the wall.
    if check("the robot's gripper is on the other side of the wall and the puck is not just above the goal location yet"):
        robot.lower("puck to the goal height")
    # Release the puck by opening the gripper.
    if check("the robot's gripper is just above the goal location and the robot's gripper is closed"):
        robot.open("gripper above goal location")