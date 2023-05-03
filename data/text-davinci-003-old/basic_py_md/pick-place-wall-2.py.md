

If check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
If check("the robot's gripper is not around the puck and the robot's gripper is open"):
    robot.grab("puck around wall")
If check("the robot's gripper is not around the puck and the robot's gripper is closed"):
    robot.push("the puck up and over the wall")
If check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
    robot.close("gripper around puck")
If check("the robot's gripper is above the puck and the robot's gripper is closed"):
    robot.place("puck at goal")