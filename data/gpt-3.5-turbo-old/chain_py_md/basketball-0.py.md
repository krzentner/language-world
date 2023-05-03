# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Move gripper above ball
    #  2. Drop gripper around ball
    #  3. Close gripper around ball
    #  4. Move gripper above hoop
    #  5. Release ball into hoop
    # First, move the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move("gripper to ball")
        robot.put("gripper above ball")
    # If the gripper isn't around the ball, put it around the ball.
    if check("the robot's gripper is not around ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # We closed the gripper, and the ball is still near the gripper, so maybe we
    # grabbed it.
    # Move the gripper above the hoop.
    if check("the robot's gripper is above ball and the robot's gripper is closed and the robot's gripper is not vertically aligned with the hoop"):
        robot.move("gripper to hoop")
        robot.put("gripper above hoop")
    # If the gripper is above the hoop, release the ball.
    if check("the robot's gripper is above hoop and the robot's gripper is closed"):
        robot.release("ball into hoop")