

Your program should move the robot's gripper to the soccer ball and push it toward the target.

# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Push down onto soccer ball
    #  3. Slide soccer ball to goal
    # First, put the gripper roughly above the soccer ball, so that we don't kick it while
    # trying to push it.
    if check("the robot's gripper is not above the soccer ball"):
        robot.place("gripper above soccer ball")
    # If the gripper is lined up with the soccer ball, push down on it.
    if check("the robot's gripper is vertically aligned with the soccer ball"):
        robot.push("down onto soccer ball")
    # Now that the gripper is pushing down on the soccer ball, we can slide it to
    # the target.
    if check("the robot's gripper is pushing down on the soccer ball"):
        robot.slide("soccer ball to goal")