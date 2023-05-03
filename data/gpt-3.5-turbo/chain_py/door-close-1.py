# Steps:
    # 1. Put gripper around door handle
    # 2. Push door closed to target location
    # First, put the gripper around the door handle.
    if check("the robot's gripper is not around the door handle"):
        robot.grab("door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed to the target location.
    if check("the robot's gripper is around door handle and the door is not closed to the target location"):
        robot.push("door closed to target location")