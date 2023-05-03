# Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # If the gripper isn't near the door handle, move it towards the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, push the door closed towards the target
    # location.
    if check("the robot's gripper is near the door handle"):
        robot.move_gripper("above the target location")