if check("the robot's gripper is not near the handle"):
        robot.put("gripper near handle")
    if check("the robot's gripper is not below the handle and the gripper is not almost horizontally aligned with handle"):
        robot.move("gripper below handle")
    if check("the robot's gripper is below the handle and the gripper is almost horizontally aligned with handle"):
        robot.push("down on handle")