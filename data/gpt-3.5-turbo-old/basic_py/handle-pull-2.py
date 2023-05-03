    if check("the robot's gripper is not near the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper to handle")
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")