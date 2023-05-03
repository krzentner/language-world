

If check("the robot's gripper is not above the puck"):
    robot.reach("above puck")
if check("the robot's gripper is above the puck and the robot's gripper is not around puck"):
    robot.drop("gripper around puck")
if check("the robot's gripper is around puck and the robot's gripper is open"):
    robot.close("gripper around puck")
if check("the robot's gripper is around the puck and the robot's gripper is closed"):
    robot.reach("to goal")
if check("the robot's gripper is near the goal"):
    robot.place("puck at goal")