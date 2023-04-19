
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    if check("the robot's gripper is above the hammer and the robot's gripper is open"):
        robot.grab("hammer")
    if check("the robot's gripper is above the hammer and the robot's gripper is closed"):
        robot.hit("nail with hammer")