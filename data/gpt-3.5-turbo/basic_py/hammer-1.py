if check("the robot's gripper is not near the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is holding the hammer"):
        robot.swing("hammer")
    if check("the hammer is above the nail"):
        robot.hit("nail with hammer")