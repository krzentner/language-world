
    if check("the cube is not nearby and the robot's gripper is not above cube"):
        robot.location("adjust to cube")
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is above cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.lift("cube")
    if check("the cube is lifted"):
        robot.place("cube at target bin")