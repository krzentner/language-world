# Steps:
    #  1. Put gripper around door handle
    #  2. Push the door closed
    # As long as the gripper isn't around the door handle, move the gripper to the
    # door handle.
    if check("the robot's gripper is not around door handle"):
        robot.grab("door handle")
    # If the gripper is around the door handle, try to push the door closed to
    # the target location.
    if check("the robot's gripper is around door handle"):
        robot.push("door closed to target location")