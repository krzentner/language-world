

If check("the robot's gripper is not above the hammer"):
    robot.put("gripper above hammer")
if check("the robot's gripper is above the hammer and the hammer is not above the nail"):
    robot.grab("hammer")
if check("the hammer is above the nail and the robot's gripper is not forward aligned with the nail"):
    robot.align("hammer to nail")
if check("the hammer is above the nail and the robot's gripper is forward aligned with the nail"):
    robot.hit("hammer on nail")