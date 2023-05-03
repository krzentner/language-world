
    if check("the robot's gripper is not above cube"):
        robot.reach("gripper above cube")
    if check("the robot's gripper is open and the robot's gripper is above cube"):
        robot.close("gripper around cube")
    if check("the robot's gripper is closed and the robot's gripper is near cube"):
        robot.sweep("cube to goal")