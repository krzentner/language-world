# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Move gripper to above the hoop
    #  5. Drop ball into the hoop
    # First, put the gripper roughly above the ball so we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper and the ball is still near the gripper, so we must have grabbed it.
    # Now move the gripper above the hoop.
    if check("the robot's gripper is above ball and the robot's gripper is closed and the hoop is not in sight"):
        robot.move("gripper to above the hoop")
    # Once the gripper is above the hoop, drop the ball into the hoop.
    if check("the robot's gripper is above the hoop and the robot's gripper is closed and the hoop is in sight"):
        robot.drop("ball into the hoop")