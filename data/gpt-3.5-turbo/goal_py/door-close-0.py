# Steps:
    #  1. Put gripper near the door handle
    #  2. Start pushing against the door to close it
    # If the gripper is not almost vertically aligned with the door handle, we
    # should move the gripper to the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # If the gripper is almost vertically aligned with the door handle and not
    # near the target location, move to the target location.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # If the gripper is near the target location, we can push the door closed.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("around the door handle")