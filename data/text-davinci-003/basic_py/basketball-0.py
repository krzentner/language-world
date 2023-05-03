
    if check("the robot's gripper is not near the basketball"):
        robot.reach("gripper to basketball")
    if check("the hoop is not lower than the robot's gripper"):
        robot.put("hoop lower than gripper")
    if check("the robot's gripper is near the basketball"):
        robot.drop("basketball into hoop")