

If check("the robot's gripper is not above the handle"):
    robot.put("gripper above handle")
if check("the robot's gripper is not around the handle and the robot's gripper is open"):
    robot.grab("gripper around handle")
if check("the robot's gripper is around the handle"):
    robot.pull("handle up")