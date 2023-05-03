# Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper is above the handle, grab it.
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # Push down on the handle.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")