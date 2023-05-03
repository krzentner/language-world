

If check("the robot's gripper is not above the hammer"):
     robot.put("gripper above the hammer")
if check("the robot's gripper is not around the handle of the hammer"):
    robot.grab("handle of hammer")
if check("the robot's gripper is not forward aligned with the nail"):
    robot.align("hammer to nail")
if check("the robot's gripper is forward aligned with the nail"):
    robot.hit("hammer on nail")