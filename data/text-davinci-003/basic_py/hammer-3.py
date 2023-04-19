
    if check("the robot's gripper is not below the hammer"):
        robot.put("gripper above hammer")
    if check("the robot's gripper is above the hammer and the robot's gripper is open"):
        robot.drop("gripper around hammer")
    if check("the robot's gripper is below the hammer and the robot's gripper is closed"):
        robot.move("hammer above the nail")
    if check("the hammer is above the nail"):
        robot.push("hammer down onto nail")