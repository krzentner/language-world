

    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is around cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is not forward aligned with the target location"):
        robot.align("gripper with target")
    if check("the robot's gripper is forward aligned with the target location"):
        robot.sweep("gripper to the target")