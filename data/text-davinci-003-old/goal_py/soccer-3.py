
    # Steps:
    #  1. Put gripper above the soccer ball
    #  2. Push the soccer ball towards the target
    # We need to put the gripper above the soccer ball first, so that we can push
    # it without it rolling away.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper is above the soccer ball, now we can push it towards the
    # target.
    if check("the robot's gripper is above the soccer ball but not near it"):
        robot.move_gripper("near the soccer ball")
    # Push harder if the soccer ball isn't close to the target.
    if check("the soccer ball is not close to the target"):
        robot.move_gripper("near the target")