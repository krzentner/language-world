# Steps:
    # 1. Put gripper around the handle
    # 2. Pull up on the handle from the side
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    # If the gripper is around the handle but not vertical, line it up so we can
    # pull it up.
    if check("the robot's gripper is around the handle and not vertically aligned with the handle"):
        robot.put("gripper vertically aligned with the handle")
    # Finally, pull up on the handle from the side.
    if check("the robot's gripper is around the handle and vertically aligned with the handle"):
        robot.pull("handle up from the side")