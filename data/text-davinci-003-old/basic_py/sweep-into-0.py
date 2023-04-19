
    if check("the robot's gripper is not near the cube"):
        robot.reach("to cube")
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around cube and the cube is not near target location"):
        robot.sweep("cube to goal")