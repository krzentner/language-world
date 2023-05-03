
    # Steps:
    #  1. Put gripper above handle
    #  2. Push down on the handle
    # We need to line up the gripper as viewed from above to press the handle.
    # If the gripper isn't lined up, move it near the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the robot's gripper is lined up, push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")