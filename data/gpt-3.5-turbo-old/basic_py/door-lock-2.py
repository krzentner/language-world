if check("the robot's gripper is not near the lock dial"):
        robot.move("gripper to lock dial")
    if check("the robot's gripper is near the lock dial and the dial is not aligned to 'locked' position"):
        robot.rotate("dial to locked position")