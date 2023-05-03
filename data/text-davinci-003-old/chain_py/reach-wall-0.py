
    # Steps:
    #  1. Reach the wall
    #  2. Reach around the wall
    #  3. Reach the target
    # We need to reach the wall first, so that the robot can move around it while
    # maintaining control.
    if check("the robot's gripper is not close to the wall"):
        robot.reach("to wall")
    # Once the robot is close to the wall, it can move around it while staying
    # close to it.
    if check("the robot's gripper is close to the wall and the robot's gripper is below the wall"):
        robot.reach("over wall")
    # Once the robot is over the wall, it can reach out and grab the target.
    if check("the robot's gripper is above the wall and the robot's gripper is not near the target"):
        robot.reach("to goal")