# hammer: hit the nail with the hammer
# def hammer(robot):
    if check("the hammer is not in the robot's gripper"):
        robot.grab("hammer")
    if check("the robot's gripper is not above the nail"):
        robot.put("gripper above nail")
    if check("the robot's gripper is above the nail and the robot's gripper is not vertically aligned with the nail"):
        robot.rotate("gripper to align with nail")
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.hit("the nail with the hammer")