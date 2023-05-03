

# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab the ball with gripper
    #  3. Reach above the hoop
    #  4. Drop the ball into the hoop
    # First, move the gripper above the ball.
    if check("the robot's gripper is not above ball"):
        robot.put("gripper above ball")
    # If the gripper is near the ball and open, try to grab the ball by closing
    # the gripper.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper, and the ball is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the ball to above the hoop.
    if check("the robot's gripper is above ball and the robot's gripper is closed"):
        robot.reach("above hoop")
    # If the ball is above the hoop, drop the the ball into the hoop.
    if check("the ball is above the hoop"):
        robot.drop("ball into hoop")