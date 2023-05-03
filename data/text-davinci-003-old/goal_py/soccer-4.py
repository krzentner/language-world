
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal
    # We need to put the gripper above the soccer ball before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with soccer ball"):
        robot.move_gripper("vertically aligned with the soccer ball")
    # Once the gripper is lined up above the soccer ball, we should be able to
    # grab the soccer ball by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not around soccer ball"):
        robot.move_gripper("around the soccer ball", close_gripper=True)
    # Once the gripper is around the soccer ball, we can just slide it to the
    # target location.
    if check("the robot's gripper is around soccer ball"):
        robot.move_gripper("above the target location")