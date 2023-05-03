

Then use the steps from the other tasks to fill in the procedure.

# soccer: push the soccer ball into the target location
# def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into top of soccer ball
    #  3. Slide soccer ball to goal
    # First, put the gripper roughly above the soccer ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper isn't around the soccer ball, put it around the soccer ball.
    if check("the robot's gripper is not around soccer ball and the robot's gripper is open"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is near the soccer ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above soccer ball and the robot's gripper is closed"):
        robot.move_gripper("above the target location")