# Steps:
    #  1. Put gripper above soccer ball
    #  2. Grab the soccer ball with the gripper
    #  3. Move the soccer ball to the target location
    # First, put the gripper roughly above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # Once the gripper is above the soccer ball, grip it securely.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is open"):
        robot.move_gripper("around the soccer ball", close_gripper=True)
    # Once we've gripped the soccer ball, we can move it to the target location
    # by moving the gripper there.
    if check("the robot's gripper is around the soccer ball and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")