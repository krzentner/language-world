

# basketball: put the ball into into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Move ball towards hoop
    #  4. Place ball in the hoop
    # First, put the gripper roughly above the ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        robot.move_gripper("near the hoop")
    # Once the ball is near the hoop, adjust the gripper's position so that it is
    # directly in front of the hoop.
    if check("the robot's gripper is near the hoop and the ball is not in front of the hoop"):
        robot.move_gripper("in front of the hoop")
    # Now that the gripper is lined up with the hoop, we can place the ball in the hoop.
    if check("the robot's gripper is in front of the hoop"):
        robot.move_gripper("above the hoop")