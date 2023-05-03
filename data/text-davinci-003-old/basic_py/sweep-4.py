
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not near the cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the cube is not left of the robot's gripper"):
        robot.move("cube to the left")
    if check("the cube is left of the robot's gripper and the robot's gripper is near the cube"):
        robot.sweep("cube to the right")