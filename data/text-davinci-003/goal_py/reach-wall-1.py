
    # Steps:
    #  1. Reach or around the wall
    #  2. Reach to the target
    # We will have to navigate around the wall before we can reach the target
    # location.
    # If the gripper is not near the wall, move it near the wall.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # If the gripper is near the wall but not near the target, try to reach
    # around the wall.
    if check("the robot's gripper is near the wall and the target is not near the robot's gripper"):
        robot.move_gripper("around the wall")
    # If the gripper is now near the target, try to reach to the target.
    if check("the robot's gripper is near the target"):
        robot.move_gripper("near the target")