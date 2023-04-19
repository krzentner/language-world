# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Position the gripper to aim at the hoop
    #  4. Release the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.put("gripper above the ball")
    # If the ball is not grabbed by the gripper, move the gripper down to grab it.
    if check("the robot's gripper is above the ball and the ball is not grabbed by the gripper"):
        robot.grab("ball")
    # After grabbing the ball, position the gripper to aim at the hoop. This may involve
    # rotating the gripper as well.
    if check("the ball is grabbed by the gripper and the gripper is not aimed at the hoop"):
        robot.position("gripper to aim at the hoop")
    # Finally, release the ball into the hoop.
    if check("the gripper is aimed at the hoop"):
        robot.release("ball into the hoop")