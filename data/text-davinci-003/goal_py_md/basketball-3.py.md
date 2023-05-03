

# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Drop gripper around ball
    #  3. Push the ball towards the hoop
    # We need to put the gripper above the ball before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # Once the gripper is lined up above the ball, we should be able to
    # grab the ball by moving the gripper down around it.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("around the ball", close_gripper=True)
    # Once the gripper is around the ball, we can start pushing the ball
    # towards the hoop.
    if check("the robot's gripper is around the ball"):
        robot.move_gripper("forward aligned with the hoop")