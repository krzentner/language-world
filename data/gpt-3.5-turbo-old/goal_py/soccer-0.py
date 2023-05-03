# Steps:
    #  1. Put gripper above the soccer ball
    #  2. Grab the soccer ball with the gripper
    #  3. Line up the soccer ball with the target location
    #  4. Push the soccer ball towards the target location
    # First, put the gripper above the soccer ball.
    if check("the robot's gripper is not vertically aligned with the soccer ball"):
        robot.move_gripper("vertically aligned with the soccer ball")
    # If the soccer ball becomes left of the gripper, go back to putting the
    # gripper above the soccer ball.
    # Because the soccer ball is a round object, check if the gripper is around
    # it instead of in front of it.
    if check("the soccer ball is not within the gripper's reach and the gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # As long the soccer ball is not lined up with the target, line it up with the
    # target.
    if check("the soccer ball is not horizontally aligned with the target and the robot's gripper is above the soccer ball"):
        robot.move_gripper("horizontally aligned with the target")
    # If the soccer ball is aligned with the target, push it to the target
    if check("the robot's gripper is horizontally aligned with the target and the gripper is closed"):
        robot.move_gripper("above the target location")