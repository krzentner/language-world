
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Push the puck to the target
    # First, put the gripper above the puck to start.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with puck", close_gripper=True)
    # If the puck ends up left of the gripper, go back to putting the gripper
    # above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("forward aligned with puck")
    # Push the puck to target by moving the gripper left.
    if check("the robot's gripper is above the puck and the robot's gripper is not horizontally aligned with target"):
        robot.move_gripper("horizontally aligned with the target")