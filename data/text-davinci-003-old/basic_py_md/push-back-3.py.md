

If check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
	robot.put("the gripper above the puck")

If check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
	robot.push("the gripper into the puck")

If check("the robot's gripper is near the puck and the puck is in front of the robot's gripper"):
	robot.back("the puck to the goal")