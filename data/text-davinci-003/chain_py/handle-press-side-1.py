
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Push down on the handle
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.put("gripper aside of handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("down on handle")