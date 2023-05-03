# basketball: put the ball into the hoop
def basketball(robot):
    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Align robot with the hoop
    #  4. Move robot closer to the hoop
    #  5. Lift the ball up to the height of the hoop
    #  6. Move robot closer to the hoop
    #  7. Align the robot with the hoop
    #  8. Move the ball towards the hoop
    #  9. Release the ball into the hoop
    # First, put the gripper above the ball
    if check("the robot's gripper is not above the ball"):
        robot.place("gripper above ball")
    # If the gripper is not around the ball, move it there
    if check("the robot's gripper is not around the ball and the robot's gripper is open"):
        robot.drop("gripper around ball")
    # If the gripper is near the ball and open, grab it
    if check("the robot's gripper is near ball and the robot's gripper is open"):
        robot.close("gripper around ball")
    # Align the robot with the hoop
    if check("the robot is not aligned with the hoop"):
        robot.align("with hoop")
    # Move closer to the hoop
    if check("the robot is not close enough to the hoop"):
        robot.move("closer to hoop")
    # Lift the ball up to the height of the hoop
    if check("the ball is not at the height of the hoop"):
        robot.lift("ball to height of hoop")
    # Move closer to the hoop
    if check("the robot is not close enough to the hoop"):
        robot.move("closer to hoop")
    # Align the robot with the hoop
    if check("the robot is not aligned with the hoop"):
        robot.align("with hoop")
    # Move the ball towards the hoop
    if check("the ball is not in front of the hoop"):
        robot.slide("ball to the hoop")
    # Release the ball into the hoop
    if check("the robot's gripper is closed and the ball is in front of the hoop"):
        robot.open("gripper")