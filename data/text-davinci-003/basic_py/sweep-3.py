
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is around cube and the robot's gripper is closed"):
        robot.sweep("cube to the goal")