if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is open and not around the cube"):
        robot.grab("cube")
    if check("the robot's gripper is around the cube and the cube is not in front of the target location"):
        robot.move("gripper to target location")
    if check("the robot's gripper is in front of the target location"):
        robot.drop("cube at target location")