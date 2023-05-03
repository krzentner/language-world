if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the dial and the dial is not at the unlocked position"):
        robot.turn("dial to unlock position")
    if check("the dial is at the unlocked position"):
        print("Door is now unlocked")