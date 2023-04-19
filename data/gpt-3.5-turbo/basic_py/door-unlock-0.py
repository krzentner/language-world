if check("the robot's gripper is not aligned with the door lock"):
        robot.move("gripper to door lock")
    if check("the robot's gripper is aligned with the door lock and the lock is not unlocked"):
        robot.turn("dial to unlock door")