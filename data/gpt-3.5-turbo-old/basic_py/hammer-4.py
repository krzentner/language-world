if check("the hammer is not in the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is above the nail"):
        robot.move("gripper above nail")
    if check("the gripper is around the handle of the hammer and the hammer's head is above the nail"):
        robot.swing("hammer")
    if check("the hammer's head is on top of the nail"):
        robot.hit("nail")