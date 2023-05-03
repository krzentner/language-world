
    if check("the robot's gripper is not above the nail"):
        robot.move("gripper above nail")
    if check("the robot's gripper is forward aligned with nail"):
        robot.align("hammer with nail")
    if check("the hammer is aligned with nail"):
        robot.hit("nail with hammer")