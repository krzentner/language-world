# Steps:
    #  1. Put the gripper on one end of the stick
    #  2. Hold the other end of the stick to slide the thermos
    # First, put the gripper on one end of the stick.
    if check("the robot's gripper is not on one end of the stick"):
        robot.move_gripper("on one end of the stick")
    # If the gripper is on one end of the stick, we can hold the other end of the
    # stick and slide the thermos.
    if check("the robot is not holding the other end of the stick and the thermos is not at the target location"):
        robot.move_gripper("near the thermos handle", close_gripper=True)
        robot.move_gripper("near the target location")