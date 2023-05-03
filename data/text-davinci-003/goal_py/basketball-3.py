
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the ball with the basket
    #  4. Throw the ball into the basket
    # First, put the gripper above the ball
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the ball becomes left of the gripper, it means that we've lost control
    # of the ball and need to regain control by grabbing it.
    # We can do this by closing the gripper and grabbing the ball with the
    # gripper.
    if check("the ball is not left of the robot's gripper"):
        robot.move_gripper("left of the ball", close_gripper=True)
    # As long as the ball is still in the gripper we can line it up with the
    # basket by moving the gripper.
    if check("the robot's gripper is vertically aligned with the ball and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the basket")
    # If the ball is in the basket, we know it's lined up correctly and can
    # throw the ball into the basket.
    if check("the robot's gripper is forward aligned with the basket"):
        robot.move_gripper("forward aligned with the basket")