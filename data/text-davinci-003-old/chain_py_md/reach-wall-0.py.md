

The robotic arm needs to reach the target location, but there is a short wall in the way.

Steps:

1. Put gripper above wall
2. Reach over wall to target location

if check("the robot's gripper is not above the wall"):
    robot.put("gripper above wall")
if check("the robot's gripper is above the wall"):
    robot.reach("over wall to target location")