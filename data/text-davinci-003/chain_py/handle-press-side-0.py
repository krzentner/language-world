
    # Steps:
    #  1. Line up the gripper with the handle as viewed from the side
    #  2. Push the handle down
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.align("gripper to handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("down on handle")