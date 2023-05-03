if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is closed around the cube and the robot is not next to the target location"):
        robot.move("sideways towards goal while holding the cube")
    if check("the robot is next to the target location"):
        robot.place("cube at goal")