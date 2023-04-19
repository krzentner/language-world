# Steps:
    #  1. Move gripper above ball and open gripper
    #  2. Move gripper towards the hoop
    #  3. Close the gripper and lift the ball
    #  4. Aim and shoot the ball into the hoop
    # First, move the gripper above the ball and open the gripper.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    if check("the robot's gripper is above the ball and the gripper is not open"):
        robot.move_gripper("near the ball", close_gripper=True)
    # Move the ball towards the hoop.
    if check("the robot's gripper is not aimed towards the hoop"):
        robot.move_gripper("aimed towards the hoop")
    # Close the gripper and lift the ball.
    if check("the robot's gripper is aimed towards the hoop and the gripper is open"):
        robot.move_gripper("above the hoop", close_gripper=True)
    # Aim and shoot the ball into the hoop.
    if check("the robot's gripper is above the hoop and the ball is grasped by the gripper"):
        robot.move_gripper("towards the hoop", open_gripper=True)