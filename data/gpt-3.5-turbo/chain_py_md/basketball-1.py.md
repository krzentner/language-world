# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper to the hoop
    #  4. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above ball")
    # If the ball is not in the gripper yet, grab it.
    if check("the robot's gripper is above the ball and the robot's gripper is open"):
        robot.grab("ball")
    # Move the gripper to the hoop if it's not already there.
    if check("the robot's gripper is not above the hoop"):
        robot.move("gripper to hoop")
    # Release the ball into the hoop by opening the gripper.
    if check("the robot's gripper is above the hoop and the robot's gripper is closed"):
        robot.release("ball into hoop")