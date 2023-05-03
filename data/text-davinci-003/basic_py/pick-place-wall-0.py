
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.move("gripper to side of wall")
    if check("the robot's gripper is above puck and the robot's gripper is closed and the puck is not above the wall"):
        robot.place("puck at goal")