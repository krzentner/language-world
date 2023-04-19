
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("the gripper at the side of the handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not near the handle"):
        robot.push("the gripper close to the handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")