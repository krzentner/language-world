
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, move the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle, we can trap it by moving the gripper
    # to the side of the handle.
    if check("the robot's gripper is above the handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, we can pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.pull("up handle")