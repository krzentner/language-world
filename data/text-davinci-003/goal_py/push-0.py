
    # Steps:
    #  1. Put gripper left of the puck
    #  2. Start pushing against the puck
    #  3. Push the puck harder
    # If the puck is right of the robot's gripper, we should move it to the
    # side to start pushing
    if check("the robot's gripper is in front of the puck"):
        robot.move_gripper("left of the puck")
    # If the puck left of the robot's gripper and the robot's gripper is not near the puck we can slide it by moving the gripper right.
    if check("the robot's gripper is right of the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("horizontally aligned with the puck")
    # If the robot's gripper is starting to be in front of the puck, push harder.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("forward aligned with the puck")