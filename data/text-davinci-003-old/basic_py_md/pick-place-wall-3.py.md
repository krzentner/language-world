

if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is above puck and the robot's gripper is closed"):
    if check("the target location is behind the wall"):
        robot.place("puck above wall")
    if check("puck is near wall and the puck is above the wall"):
        robot.pass("puck over wall")
    if check("puck is past the wall and the robot's gripper is closed"):
        robot.place("puck at goal")