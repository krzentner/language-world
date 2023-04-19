# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line the ball up with the hoop
    #  4. Throw or place the ball into the hoop
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the ball isn't inside the gripper yet, grab it.
    if check("the robot's gripper is not around the ball" and "the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # Once the ball is in the gripper, move it to a position in front of the hoop.
    if check("the robot's gripper is around the ball and is not almost vertically aligned with the hoop"):
        robot.move_gripper("almost vertically aligned with the hoop")
    # Finally, release the gripper to throw or place the ball into the hoop.
    if check("the robot's gripper is vertically aligned with the hoop" and "the robot's gripper is closed"):
        robot.move_gripper("above the hoop", close_gripper=False)