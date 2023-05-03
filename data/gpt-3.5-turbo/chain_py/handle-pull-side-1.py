# Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up on the handle from the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Once the gripper is mostly above the handle, dropping it around the handle
    # should align it perfectly.
    if check("the robot's gripper is almost vertically aligned with handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle, pull up on the handle from the side.
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle from the side")