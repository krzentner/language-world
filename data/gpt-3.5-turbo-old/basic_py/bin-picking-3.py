if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.move("cube to target bin")
    robot.open("gripper to drop cube into bin")