
    # Steps:
    #  1. Put gripper near door handle
    #  2. Push door closed
    # We need to put the gripper near the door handle before pushing.
    # We don't need to be careful about the alignment, because we're just pushing
    # it, unlike when opening the door.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # As long as the gripper is forward aligned with the door handle, we can
    # just push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("left of the target location")