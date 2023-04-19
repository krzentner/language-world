

if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is below the handle"):
    robot.move("gripper to right of handle")
if check("the robot's gripper is near the handle"):
    robot.pull("up on handle")
if check("the robot's gripper is in front of the handle"):
    robot.pull("up on handle harder")