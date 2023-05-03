if check("the robot's gripper is not above the cube"):
    robot.move("gripper above cube")
if check("the robot's gripper is not around the cube and the gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near the cube and the gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above the target bin"):
    robot.move("gripper to target bin")
if check("the robot's gripper is near the target bin and the gripper is closed"):
    robot.drop("cube into target bin")