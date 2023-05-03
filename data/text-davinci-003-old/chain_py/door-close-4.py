
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # Move the gripper to the door handle if it is not near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the gripper is near the door handle, start pushing the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
    # If the door handle is not near the target location, keep pushing the door
    # closed until it is.
    if check("the door handle is not near the target location"):
        robot.push("door closer to target location")