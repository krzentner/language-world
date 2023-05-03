
    if check("the robot's gripper is not above puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("puck is between robot's gripper and the wall"):
        robot.push("puck over wall")
    if check("the robot's gripper is above the puck"):
        robot.place("puck at goal")