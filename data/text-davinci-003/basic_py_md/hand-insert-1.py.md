

If check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
If check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
If check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
If check("the robot's gripper is near the target location and the puck is not in the target location"):
    robot.move("puck to goal")
If check("the robot's gripper is near the target location and the puck is in the target location"):
    robot.open("gripper")