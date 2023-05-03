# Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Push ball towards goal
    # First, put the gripper roughly above the ball, so that we don't bump it
    # while trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper, and the ball is still near the gripper, so maybe we
    # grabbed it. Try to push the ball towards the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        robot.push("ball towards goal")