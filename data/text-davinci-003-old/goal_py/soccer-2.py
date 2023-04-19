
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push soccer ball in the target direction
    # First, the robot needs to move the gripper above the soccer ball.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # Once the gripper is above the soccer ball, the robot can push it with the
    # gripper.
    if check("the robot's gripper is above the soccer ball"):
        robot.move_gripper("towards the target location")