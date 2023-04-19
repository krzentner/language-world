
    if check("the robot's gripper is not forward aligned with handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is forward into handle and the robot's gripper is not touching the handle"):
        robot.push("gripper into handle")
    if check("the robot's gripper is touching the handle"):
        robot.push("handle down")