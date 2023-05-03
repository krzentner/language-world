
    # Steps:
    #  1. Put gripper above the lock handle
    #  2. Drop gripper around lock handle
    #  3. Turn lock handle clockwise
    # Put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with lock handle"):
        robot.put("gripper above lock handle")
    # If the gripper isn't near the handle, drop the gripper around it.
    if check("the robot's gripper is vertically aligned with the lock handle and the robot's gripper is not near lock handle"):
        robot.drop("gripper around lock handle")
    # If the gripper is near the handle, we can probably turn the handle.
    if check("the robot's gripper is near lock handle"):
        robot.rotate("clockwise")