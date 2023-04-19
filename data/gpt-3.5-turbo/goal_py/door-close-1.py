# Steps:
    #  1. Put the gripper near the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the door is not almost closed, we can start pushing the door closed.
    if check("the door is not almost closed"):
        robot.move_gripper("horizontally aligned with the door handle")