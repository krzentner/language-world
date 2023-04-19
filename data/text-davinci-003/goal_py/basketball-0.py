
    # Steps:
    #  1. Place the gripper directly above the ball
    #  2. Drop the gripper around the ball
    #  3. Move the gripper towards the hoop
    #  4. Drop the ball into the hoop
    # First, put the gripper above the ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # If the gripper is around the ball, we can move to the hoop.
    if check("the robot's gripper is around ball"):
        robot.move_gripper("near the hoop")
    # If the gripper has reached the hoop, drop the ball into the hoop.
    if check("the robot's gripper is near the hoop"):
        robot.move_gripper("above the hoop")