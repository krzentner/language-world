
    if check("the robot's gripper is not forward aligned with the mug"):
        robot.reach("gripper to mug")
    if check("the robot's gripper is forward aligned with the mug and the robot's gripper is not grasped the mug"):
        robot.grab("mug")
    if check("the robot's gripper is grasped the mug and the robot is not near target location"):
        robot.pull("mug to target")