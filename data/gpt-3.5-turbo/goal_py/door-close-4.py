# Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed to the target location
    # If the gripper is not near the door handle, move it to the door handle.
    # Because the door is larger than the gripper, we don't need to be careful
    # about the direction.
    if check("the robot's gripper is not near the door handle"):
        robot.move_gripper("near the door handle")
    # If the gripper is near the door handle, push the door closed to the target
    # location.
    if check("the robot's gripper is around the door handle"):
        robot.move_gripper("vertically aligned with the target location")