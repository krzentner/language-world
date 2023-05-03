# Steps:
    #  1. Line up the gripper with the ball
    #  2. Pick up the ball
    #  3. Line up the gripper with the hoop
    #  4. Drop the ball into the hoop
    # Line up the gripper with the ball.
    if check("the robot's gripper is not vertically aligned with ball and the robot's gripper is not around the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # Once the gripper is lined up above the ball, we should be able to grab the ball by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with ball and the robot's gripper is not around ball"):
        robot.move_gripper("around the ball", close_gripper=True)
    # Once the gripper is around the ball, we can position it to be dropped into the hoop.
    if check("the robot's gripper is around ball and the robot's gripper is not above the hoop"):
        robot.move_gripper("above the hoop")
    # Once the gripper is above the hoop we can drop the ball into the hoop by opening the gripper.
    if check("the robot's gripper is above the hoop and the robot's gripper is not open"):
        robot.move_gripper("around the ball", close_gripper=False)