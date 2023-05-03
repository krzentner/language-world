
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not near cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the cube is not left of the robot's gripper"):
        robot.move("cube left of gripper")
    if check("the cube is left of the robot's gripper and the robot's grip is closed"):
        robot.sweep("cube across to goal")