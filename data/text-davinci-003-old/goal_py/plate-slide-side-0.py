
    # Steps:
    #  1. Put gripper right of the plate
    #  2. Start pushing against the plate to slide it
    #  3. Push the plate harder
    # If the robot's gripper is not right of the plate, we should move the
    # gripper near the plate to start pushing
    if check("the robot's gripper is not right of the plate"):
        robot.move_gripper("right of the plate")
    # If the robot's gripper is near the plate, we can probably slide the plate
    # now by moving the gripper left.
    if check("the robot's gripper is right of the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate")
    # If the robot's gripper is starting to be in front of the plate, push
    # harder.
    if check("the robot's gripper is near the plate"):
        robot.move_gripper("left of the plate")