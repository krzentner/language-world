

Steps:
1. Put the gripper above the mug
2. Drop the gripper around the mug
3. Close the gripper around the mug
4. Pull the mug to the target location

if check("the robot's gripper is not above the mug"):
    robot.put("gripper above mug")
if check("the robot's gripper is not around the mug and the robot's gripper is open"):
    robot.drop("gripper around mug")
if check("the robot's gripper is near the mug and the robot's gripper is open"):
    robot.close("gripper around mug")
if check("the robot's gripper is around the mug and the mug is below the robot's gripper"):
    robot.pull("mug to the goal")