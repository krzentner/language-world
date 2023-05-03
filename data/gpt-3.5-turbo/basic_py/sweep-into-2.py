def sweep_into(robot):
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("cube is not near robot's gripper"):
        robot.move("gripper towards cube")
    if check("the robot's gripper is near and above the cube"):
        robot.grab("cube")
    if check("the robot's gripper is closed and the cube is not at the target location"):
        robot.slide("cube to target location")
    if check("the robot's gripper is at the target location and holding the cube"):
        robot.drop("cube at target location")