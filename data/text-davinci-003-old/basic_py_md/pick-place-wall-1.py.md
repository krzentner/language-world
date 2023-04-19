

if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is above puck and the puck is below the wall"):
    robot.lift("puck over wall")
if check("the robot's gripper is above the puck and the puck is above the wall"):
    robot.place("puck at goal")