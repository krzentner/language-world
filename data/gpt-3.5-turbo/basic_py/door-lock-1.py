if check("the robot's gripper is not near the door lock and the robot's gripper is open"):
        robot.grab("door lock")
    if check("the robot's gripper is around the door lock"):
        robot.rotate("the dial to the locked position")