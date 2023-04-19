
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push forward back of soccer ball
    #  3. Push soccer ball towards target location
    # Place the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the back of the soccer ball is not left of the robot's gripper, move
    # the robot's gripper to the left of the back of the soccer ball.
    if check("the robot's gripper is left of the back of the soccer ball and the robot's gripper is not on the back of the soccer ball"):
        robot.move_gripper("on the back of the soccer ball", close_gripper=True)
    # If the gripper is on the back of the soccer ball and the soccer ball is
    # not in the target location, move the gripper right to push the soccer
    # ball towards the target location.
    if check("the robot's gripper is on the back of the soccer ball and the soccer ball is not in the target location"):
        robot.move_gripper("above the target location")