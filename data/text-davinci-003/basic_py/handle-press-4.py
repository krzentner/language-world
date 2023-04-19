
    if check("the robot's gripper is not below the door handle"):
        robot.put("gripper below door handle")
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is closed"):
        robot.push("down on handle")