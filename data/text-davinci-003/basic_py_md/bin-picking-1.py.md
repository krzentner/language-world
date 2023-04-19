

If check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
If check("the robot's gripper is not around the cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
If check("the robot's gripper is near the cube and the robot's gripper is open"):
    robot.close("gripper around cube")
If check("the robot's gripper is above the cube and the robot's gripper is closed"):
    robot.move("gripper over target bin")
If check("the robot's gripper is above the target bin and the robot's gripper is closed"):
    robot.drop("cube into bin")