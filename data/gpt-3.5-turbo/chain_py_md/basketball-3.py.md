# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Move above the ball
    #  2. Lower the gripper and grab the ball
    #  3. Move to the hoop
    #  4. Raise the gripper and release the ball into the hoop
    # First, move the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move("gripper above ball")
    # If the gripper is above the ball, lower the gripper to grab the ball.
    if check("the robot's gripper is above the ball and the robot's gripper is not close to the ball"):
        robot.grab("ball")
    # Move the ball to the hoop.
    if check("the robot's gripper has the ball and is not above the hoop"):
        robot.move("ball to hoop")
    # If the gripper is above the hoop, raise the gripper to release the ball.
    if check("the robot's gripper is above the hoop and the robot's gripper has the ball"):
        robot.release("ball into hoop")