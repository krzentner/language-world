if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.move("gripper to handle")
    if check("the robot's gripper is near the handle"):
        robot.push("down on handle")