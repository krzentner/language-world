
    if check("the robot's gripper is not above cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.slide("cube to goal")
    if check("the robot's gripper is at goal and the cube is not at goal"):
        robot.push("cube to goal")