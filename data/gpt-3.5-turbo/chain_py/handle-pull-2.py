# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper is not around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, pull it up.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")