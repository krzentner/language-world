# Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction since we're just pushing the door
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door handle is aligned with the gripper from in front, we can push the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.move_gripper("around the door handle")