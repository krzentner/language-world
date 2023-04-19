
    # Steps:
    #  1. Reach around the wall
    #  2. Reach to the target
    # To reach around the wall, the robot's gripper should go around the left
    # side of the wall first.
    if check("the wall is between the robot and target and the robot's gripper is not around the left side of the wall"):
        robot.reach("around the wall")
    # After the robot's gripper goes around the left side of the wall, it should
    # reach to the target.
    if check("the robot's gripper is around the left side of the wall"):
        robot.reach("to target")