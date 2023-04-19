
    # Steps:
    #  1. Put gripper above ball
    #  2. Drop gripper around ball
    #  3. Put ball towards the hoop
    # First, put the gripper above the ball 
    if check("the robot's gripper is not above the ball"):
        robot.put("gripper above the ball")
    # Once the gripper is above the ball, grab the ball 
    if check("the robot's gripper is above the ball and the robot's gripper is not around the ball"):
        robot.drop("gripper around the ball")
    # Now that the gripper is around the ball, shoot the ball towards the hoop 
    if check("the robot's gripper is around the ball"):
        robot.put("ball towards the hoop")