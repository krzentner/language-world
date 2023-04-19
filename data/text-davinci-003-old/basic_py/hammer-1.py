
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    if check("the robot's gripper is not forward aligned with the nail"):
        robot.align("gripper with nail")
    if check("the robot's gripper is forward aligned with the nail and the robot's gripper is not near the nail"):
        robot.put("gripper near nail")
    if check("the robot's gripper is near the nail and the hammer's head is not above the nail"):
        robot.put("hammer's head above nail")
    if check("the hammer's head is above the nail"):
        robot.hit("nail with hammer")