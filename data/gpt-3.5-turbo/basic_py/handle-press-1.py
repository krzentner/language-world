if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the handle is not already pressed"):
        robot.push("down on handle")
    if check("the handle is pressed"):
        robot.move("gripper away from handle")