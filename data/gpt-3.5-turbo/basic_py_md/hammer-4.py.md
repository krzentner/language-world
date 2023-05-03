# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not almost vertically aligned with hammer handle"):
        robot.put("gripper above hammer handle")
    if check("the robot's gripper is almost vertically aligned with hammer handle and the robot's gripper is open"):
        robot.put("gripper around hammer handle")
    if check("the robot's gripper is around hammer handle and the robot's gripper is not above the nail"):
        robot.move("gripper above nail")
    if check("the robot's gripper is above the nail and the robot's gripper is not around the hammer handle"):
        robot.pull("hammer up")
    if check("the robot's gripper is above the nail and the robot's gripper is around the hammer handle"):
        robot.push("hammer down onto nail")