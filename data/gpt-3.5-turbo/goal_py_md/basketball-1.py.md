# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the gripper with the hoop
    #  4. Throw the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the ball is not in the gripper, grab it.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.move_gripper("around the ball", close_gripper=True)
    # If the gripper is lined up with the hoop, throw the ball.
    if check("the robot's gripper is forward aligned with the hoop"):
        robot.move_gripper("near the hoop", close_gripper=False)
    
# check function to simulate a check to see if the current action is completed
def check(task):
    print("Check:", task)
    return True