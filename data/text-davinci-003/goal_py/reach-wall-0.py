
    # Steps:
    #  1. Reach up and around the wall towards the target
    # To get over the wall, first position the gripper just above it.
    if check("the robot's gripper is not just above the wall"):
        robot.move_gripper("just above the wall")
    # Now, we can move around the wall to the target.
    if check("the robot's gripper is forward aligned with the wall"):
        robot.move_gripper("above the reach target")