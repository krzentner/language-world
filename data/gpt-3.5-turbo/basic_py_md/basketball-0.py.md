# basketball: put the ball into the hoop
# def basketball(robot):
def basketball(robot):
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    if check("the robot's gripper is near the ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    if check("the robot's gripper is above the hoop and the robot's gripper is closed"):
        robot.place("ball into hoop") 

# This program defines the function `basketball` that takes in a `robot` argument and is responsible for putting the ball into the hoop using the robot's single gripper. It starts by checking if the robot's gripper is not above the ball and if so, moves it to be placed above the ball.
# The if statement checks if the gripper is not around the ball and the gripper is open yet, drops it around the ball. If the gripper is already around the ball and close, check if the gripper is above the hoop and placed the ball into the hoop.