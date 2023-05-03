# window-close: slide the window closed to the right
# def window_close(robot):
if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
    robot.move("gripper to left of window handle")
if check("the robot's gripper is near the window handle"):
    robot.slide("window right")
if check("the robot's gripper is in front of the window handle"):
    robot.push("window right harder") 

# create an instance of the robot
robot = Robot()

# call the function to close the window
window_close(robot)