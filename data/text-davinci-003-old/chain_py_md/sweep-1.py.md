

Steps:
1. Put gripper above cube
2. Drop gripper around cube
3. Close gripper around cube
4. Sweep cube to the goal

if check("the robot's gripper is not above cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is around cube and the robot's gripper is closed"):
    robot.sweep("cube to goal")