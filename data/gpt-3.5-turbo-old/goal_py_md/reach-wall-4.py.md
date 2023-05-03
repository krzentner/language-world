# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
    # Steps:
    #  1. Check if there is a wall blocking the way
    #  2. Use a side movement to go around the wall if it exists
    #  3. Reach towards the target
    # Check if there is a wall blocking the way to the target
    if check("there is a wall blocking the robot's path to the target"):
        # Move the robot to the left of the wall
        if check("the robot is not left of the wall"):
            robot.move_gripper("left of the wall")
        # Move the robot forward and to the right of the wall
        if check("the robot is not forward and right of the wall"):
            robot.move_gripper("forward and right of the wall")
    # Move the gripper towards the target now that the wall is out of the way
    if check("the robot's gripper is not near the reach target"):
        robot.move_gripper("near the reach target")