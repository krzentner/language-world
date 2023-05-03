

Steps: 
    1. Put the gripper above the ball
    2. Drop the gripper around the ball
    3. Move the Gripper to the basketball hoop
    4. Drop the ball into the basketball hoop


# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Move gripper to the basketball hoop
    #  4. Drop ball into hoop

    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    # If the gripper isn't near the ball, put it around the ball.
    if check("the robot's gripper is not near the ball"):
        robot.move_gripper("near the ball", close_gripper=True)
    # Once we have the ball, move the gripper to the hoop.
    if check("the robot's gripper is near the ball and the gripper is closed"):
        robot.move_gripper("above the basketball hoop")
    # When we are near the hoop but above it, drop the ball into the hoop.
    if check("the robot's gripper is is not above the basketball hoop but is near the basketball hoop"):
        robot.move_gripper("above the basketball hoop", open_gripper=True)