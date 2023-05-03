# window-close: slide the window closed to the right
# def window_close(robot):
if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
    robot.move("gripper to left of window handle")
    robot.slide("window right")
elif check("the robot's gripper is near the window handle"):
    robot.slide("window right")
else:
    robot.push("window right harder")