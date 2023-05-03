# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Approach the ball
    #  2. Trap the ball below the gripper
    #  3. Position the ball in front of the target location
    #  4. Push the ball into the target location

    # Approach the ball by moving the gripper down to it
    if check("the robot's gripper is not near the ball"):
        robot.move_gripper("near the ball")

    # Trap the ball by lowering the gripper onto it and closing the gripper
    if check("the robot's gripper is not around the ball"):
        robot.move_gripper("around the ball", close_gripper=True)

    # Position the ball in front of the target location
    if check("the ball is not in front of the target location"):
        robot.move_gripper("above the target location", close_gripper=True)

    # Push the ball into the target location
    if check("the robot's gripper is not close to the target location"):
        robot.move_gripper("close to the target location")