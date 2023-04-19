
    if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is around handle and the handle is below the robot's gripper"):
        robot.pull("upward")