
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Push the door closed
    # First, put the gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # Once the gripper is near the door handle, we can just push the door
    # closed.
    if check("the robot's gripper is near the door handle"):
        robot.push("door closed")