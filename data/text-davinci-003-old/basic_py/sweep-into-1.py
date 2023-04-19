
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above the cube and the robot's gripper is not near the cube"):
        robot.drop("gripper near cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is closed"):
        robot.sweep("cube to goal")