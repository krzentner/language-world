
    # Steps:
    #  1. Reach to the wall
    #  2. Reach around the wall
    #  3. Reach to the target
    # First, reach to the wall.
    if check("the robot's gripper is not near the wall"):
        robot.reach("to wall")
    # If the gripper is near the wall and the target is not near the gripper,
    # then we can reach around the wall.
    if check("the robot's gripper is near the wall and the target is not near the robot's gripper"):
        robot.reach("around wall")
    # If the target is near the robot's gripper, we can reach to the target.
    if check("the target is near the robot's gripper"):
        robot.reach("to target")