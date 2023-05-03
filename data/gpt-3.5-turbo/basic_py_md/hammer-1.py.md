# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not near the hammer handle"):
        robot.grab("hammer handle")
    if check("the hammer is not positioned above the nail and the robot's gripper is open"):
        robot.place("hammer above nail")
    if check("the hammer is positioned above the nail and the robot's gripper is open"):
        robot.drop("gripper around hammer handle")
    if check("the robot's gripper is holding the hammer and the hammer is above the nail"):
        robot.hit("nail with hammer")