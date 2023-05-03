
    if check("the robot's gripper is not near handle"):
        robot. grab("handle")
    if check(" the robot's gripper is near handle and the gripper is not horizontally aligned with handle"):
        robot.align("gripper with handle")
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.pull("handle up")