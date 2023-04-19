

Steps:
1. Put the gripper to the side of the wall, in line with the target location
2. Reach towards the target

if check("the robot's gripper is not to the side of the wall"):
    robot.put("gripper to the side of the wall")
if check("the robot's gripper is to the side of the wall"):
    robot.reach("to goal")