

Steps:
1. Put gripper above the lever
2. Drop the gripper around lever
3. Pull the lever up

if check("the robot's gripper is not above the lever"):
    robot.put("gripper above lever")
if check("the robot's gripper is not around lever and the robot's gripper is open"):
    robot.drop("gripper around lever")
if check("the robot's gripper is around lever"):
    robot.pull("lever up")