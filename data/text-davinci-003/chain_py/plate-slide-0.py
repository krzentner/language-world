
    # Steps:
    #  1. Put gripper above plate
    #  2. Push plate to target
	# Put the gripper above the plate so we can start to move it without
    # bumping against it.
    if check("the robot's gripper is not above plate and the robot's gripper is not near plate"):
        robot.put("gripper above plate")
    # If the gripper is near the plate, then start sliding it. 
    if check("the robot's gripper is near plate and the robot's gripper is not touching plate"):
        robot.push("plate to goal")