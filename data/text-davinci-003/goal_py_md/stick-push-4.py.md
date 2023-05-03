

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
	# Steps: 
	#1. Put the gripper above the stick
	#2. Drop the gripper around the stick
	#3. Close the gripper around the stick
    #4. Push the stick against the thermos, leading it to the target location

    # First, put the gripper roughly above the stick, so that we don't bump it while trying to grab it.
	if check("the robot's gripper is not above the stick"):
		robot.move_gripper("above the stick")

    # If the gripper isn't around the stick, close the gripper around the stick.
	if check("the robot's gripper is not around stick and the robot's gripper is open"):
		robot.move_gripper("near the stick", close_gripper=True)
	
    # If the gripper is near the stick and closed, use the stick to push the thermos.
	if check("the robot's gripper is near the stick and the robot's gripper is closed"):
		robot.move_gripper("left of the thermos")

    # If the thermos is to the left of the robot's gripper and the gripper is still closed around the stick, push the thermos to the target location.
	if check("the thermos is left of the robot's gripper and the robot's gripper is closed"):
		robot.move_gripper("near the target location")