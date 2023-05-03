# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not almost vertically aligned with hammer handle"):
        robot.put("gripper above hammer handle")
    if check("the robot's gripper is almost vertically aligned with the hammer handle and the robot's gripper is open"):
        robot.put("gripper around hammer handle")
    if check("the robot's gripper is vertically aligned with the hammer handle and the hammer is not gripped"):
        robot.grab("hammer handle")
    if check("the robot's gripper is back from the nail and the hammer is gripped"):
        robot.push("gripper forward toward the nail")
    if check("the robot's gripper is near the nail and the gripper is not open and the hammer is gripped"):
        robot.swing("the hammer to hit the nail")
    if check("the gripper is back from the nail and the hammer is gripped"):
        robot.pull("gripper back from nail")
    if check("the gripper is back from the hammer handle and the hammer is gripped"):
        robot.put("gripper above hammer handle")
    if check("the gripper is back from the hammer handle and the gripper is not open"):
        robot.open("the gripper")