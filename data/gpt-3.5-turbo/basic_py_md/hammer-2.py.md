# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not almost vertically aligned with the hammer handle"):
        robot.put("gripper above hammer handle")
    if check("the gripper is almost vertically aligned with the hammer handle and the gripper is open"):
        robot.grab("hammer handle")
    if check("the hammer is in the robot's gripper and the robot's gripper is located above the nail"):
        robot.put("hammer above nail")
    if check("the robot's gripper is directly above the nail and the hammer is in the robot's gripper"):
        robot.push("hammer down onto nail")