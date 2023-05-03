
    if check("the robot's gripper is not left of cube and the robot's gripper is not forward aligned with the cube"):
        robot.put("gripper left of cube")
    if check("the robot's gripper is left of cube and the robot's gripper is not near the cube"):
        robot.reach("towards cube")
    if check("the robot's gripper is near cube and the robot's gripper is not around cube"):
        robot.open("gripper around cube")
    if check("the robot's gripper is around cube"):
        robot.sweep("cube to goal")