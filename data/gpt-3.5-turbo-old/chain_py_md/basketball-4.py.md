# basketball: put the ball into the hoop
# def basketball(robot):
    # Steps:
    #  1. Grab the ball
    #  2. Move the ball above the hoop
    #  3. Drop the ball into the hoop
    
    # Put the gripper near the ball
    if check("the robot's gripper is not near the ball and the robot's gripper is not around the ball"):
        robot.grab("the ball")
    
    # Move the gripper above the hoop
    if check("the robot's gripper is not above the hoop"):
        robot.move("the gripper above the hoop")
    
    # Drop the ball into the hoop
    if check("the robot's gripper is above the hoop and the ball is inside the hoop"):
        robot.drop("the ball into the hoop")