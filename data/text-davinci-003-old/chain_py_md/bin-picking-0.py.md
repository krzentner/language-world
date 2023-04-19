

The steps are as follows:

1. Put the gripper above the cube
2. Drop the gripper around the cube
3. Close the gripper around the cube
4. Move the cube to the target bin

if check("the robot's gripper is not above the cube"):
    robot.put("gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move("cube to target bin")