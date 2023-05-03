# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the hammer is not in the robot's gripper"):
        robot.grab("hammer handle")
    if check("the robot's gripper is forward aligned with the nail and the hammer is in the robot's gripper"):
        robot.hit("nail with hammer")