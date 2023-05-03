
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed and the puck is not in reach of the wall"):
        robot.move("puck in reach of wall")
    if check("the robot's gripper is above puck and the robot's gripper is closed and the puck is in reach of the wall"):
        robot.place("puck at goal and near wall")