

if check("the robot's gripper is not near the cube"):
    robot.reach("to cube")
if check("the robot's gripper is not around the cube"):
    robot.grab("cube")
if check("the robot's gripper is not near the goal"):
    robot.reach("to goal")
if check("the robot's gripper is near the goal"):
    robot.sweep("cube into goal")