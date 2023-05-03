# basketball: put the ball into into the hoop
def basketball(robot):
    # Steps:
    #  1. Put the gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the gripper with the hoop
    #  4. Move the arm and release the ball
    # First, put the gripper above the ball.
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above ball")
    # If the ball is not grabbed by the gripper, grab it.
    if check("the ball is not grabbed by the gripper"):
        robot.grab("ball")
    # If the gripper is not aligned with the hoop, align it.
    if check("the robot's gripper is not aligned with the hoop"):
        robot.align("gripper to hoop")
    # Move the arm and release the ball into the hoop.
    if check("the robot's gripper is aligned with the hoop"):
        robot.move("and release the ball into the hoop")