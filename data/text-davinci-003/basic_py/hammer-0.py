
    if check("the robot's gripper is not near the hammer and the robot's gripper is not near the nail"):
        robot.place("gripper to left of hammer")
    if check("the robot's gripper is near the hammer and the robot's gripper is closed"):
        robot.open("gripper")
    if check("the robot's gripper is near the hammer and the robot's gripper is open"):
        robot.grab("hammer")
    if check("the robot's gripper is forward aligned with the nail and the robot's gripper is closed"):
        robot.hit("nail with hammer")