

If check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is below the handle"):
    robot.move("gripper to right of handle")
if check("the robot's gripper is near the handle"):
    robot.grab("handle")
if check("the robot's gripper is above the handle and the robot's gripper is not forward aligned with the handle"):
    robot.align("gripper forward with handle")
if check("the robot's gripper is forward aligned with the handle"):
    robot.pull("handle up")