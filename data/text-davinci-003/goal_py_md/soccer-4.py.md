

Steps:
1. Put gripper above soccer ball
2. Push gripper into the top of soccer ball
3. Slice soccer ball to the target location

# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push gripper into the top of soccer ball
    #  3. Slice soccer ball to the target location
    # First, put the gripper roughly above the soccer ball, so that we don't has bump it while trying to push it.
    if check("the robot's gripper is not above the soccer ball"):
        robot.move_gripper("above the soccer ball")
    # If the gripper isn't around the soccer ball, move it to the soccer ball. We don't need to be careful about the direction, since
    # the soccer ball is large and we're just pushing it.
    if check("the robot's gripper is above the soccer ball and the robot's gripper is not near the soccer ball"):
        robot.move_gripper("near the soccer ball", close_gripper=True)
    # If the gripper is starting to be in front of the soccer ball, push
    # harder.
    if check("the robot's gripper is near the soccer ball"):
        robot.move_gripper("into the soccer ball")
    # Finally, if the soccer ball is trapped and the gripper is near it, we
    # can finally push it to the target location
    if check("the robot's gripper is above the soccer ball and the soccer ball is below the robot's gripper"):
        robot.move_gripper("above the target location")