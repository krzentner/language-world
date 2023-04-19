
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around the cube and the cube is not left of the robot's gripper"):
        robot.slide("cube to the left")
    if check("the cube is left of the robot's gripper"):
        robot.slide("cube to the right")