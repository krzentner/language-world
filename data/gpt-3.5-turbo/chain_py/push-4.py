# Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Push the puck towards the target
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can push it by closing
    # the gripper.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper around the puck, and it's still near the gripper, so
    # now we can push it.
    if check("the robot's gripper is closed around puck"):
        robot.slide("puck to goal")