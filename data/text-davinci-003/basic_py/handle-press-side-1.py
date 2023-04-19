
    if check("the handle is not left of the gripper"):
        robot.put("gripper to side of handle")
    if check("the robot's gripper is vertically aligned with the handle and the handle is not forward aligned with the robot's gripper"):
        robot.push("side of handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not down"):
        robot.drop("gripper to depress handle")