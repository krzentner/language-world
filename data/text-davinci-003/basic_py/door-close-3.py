
    if check("the robot's gripper is not near the door handle"):
        robot.put("the gripper above the door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("the gripper around the door handle")
    if check("the robot's gripper is near the door handle"):
        robot.push("the door closed")