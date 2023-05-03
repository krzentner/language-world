if check("the robot's gripper is not near the mug"):
        robot.move("gripper to mug handle")
    if check("the mug handle is inside the gripper and the robot's gripper is not near the target location"):
        robot.pull("mug to target location")
    if check("the mug is at target location and the robot's gripper is open"):
        robot.drop("mug")