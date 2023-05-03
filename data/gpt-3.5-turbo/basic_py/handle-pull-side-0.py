if check("the robot's gripper is not near the handle"):
        robot.move("gripper to the side of the handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("up on the handle")