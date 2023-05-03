if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around cube"):
        robot.grab("cube")
    if check("the robot's gripper is not aligned with the target location"):
        robot.move("gripper to side of target location")
    if check("the robot's gripper is aligned with the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is holding the cube at the target location"):
        robot.drop("cube")