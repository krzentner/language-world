

If check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
if check("the robot's gripper is not around puck and the robot's gripper is open"):
    robot.drop("gripper around puck")
if check("the robot's gripper is near puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is above the puck and the robot's gripper is closed"):
    robot.check("if wall is in the way")
if check("there is a wall in the way of the goal"):
    robot.move("wall out of the way")
if check("the wall is out of the way"):
    robot.place("puck at goal")