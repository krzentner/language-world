

If check("the robot's gripper is not above the hammer"):
    robot.put("gripper above hammer")
if check("the robot's gripper is not around hammer and the robot's gripper is open"):
    robot.drop("gripper around hammer")
if check("the robot's gripper is around hammer and the robot's gripper is closed"):
    robot.strike("hammer onto nail")