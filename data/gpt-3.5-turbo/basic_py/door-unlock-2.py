if check("the robot's gripper is not almost vertically aligned with door lock dial"):
        robot.move("gripper above door lock dial")
    if check("the robot's gripper is almost vertically aligned with the door lock dial"):
        robot.grab("door lock dial")
        robot.turn("door lock dial to unlock")