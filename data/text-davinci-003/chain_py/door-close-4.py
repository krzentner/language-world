
    # Steps:
    # 1. Put gripper partially around the door handle
    # 2. Push against the door handle to close the door
    # 3. Push the door shut
    # If the gripper is not near the door handle, move it to the door
    # handle.
    if check("the robot's gripper is not near the door handle"):
        robot.put("gripper partially around door handle")
    # If the gripper is near the door handle, push against it to close.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")
    # Push harder if the robot's gripper is in front of the door handle.
    if check("the robot's gripper is in front of the door handle"):
        robot.push("door closed harder")