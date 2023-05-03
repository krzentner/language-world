
    # Steps:
    #  1. Put gripper around the door handle
    #  2. Push the door closed
    # If the robot's gripper is not around the door handle, grab the door handle.
    if check("the robot's gripper is not around the door handle"):
        robot.grab("door handle")
    # If the robot's gripper is around the door handle, we can push the door
    # closed.
    if check("the robot's gripper is around the door handle"):
        robot.push("door closed")