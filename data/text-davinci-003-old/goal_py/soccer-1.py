
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Drop gripper around soccer ball
    #  3. Push soccer ball to goal
    # First, we need to put the gripper above the soccer ball by moving the
    # gripper vertically.
    if check("the robot's gripper is not vertically aligned with soccer ball"):
        robot.move_gripper("vertically aligned with the soccer ball", close_gripper = True)
    # Once the gripper is lined up above the soccer ball, we should be able to
    # trap the soccer ball by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not around soccer ball"):
        robot.move_gripper("near the soccer ball")
    # After the gripper is around the soccer ball, just start pushing the soccer
    # ball to the target location.
    if check("the robot's gripper is around soccer ball"):
        robot.move_gripper("above the target location")