# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Drop gripper around soccer ball
    #  3. Close gripper around soccer ball
    #  4. Move soccer ball to goal
    # First, put the gripper roughly above the soccer ball, so that we don't
    # knock it away while trying to grab it.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper isn't around the soccer ball, put it around the soccer ball.
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball and closed, maybe we can grab it by
    # pushing the soccer ball into the goal with the gripper.
    if check("the robot's gripper is above soccer ball and the robot's gripper is closed"):
        robot.move_gripper("above the target location")