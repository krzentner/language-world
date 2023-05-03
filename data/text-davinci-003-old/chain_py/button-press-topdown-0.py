
    # Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # First, we need to put the gripper above the button.
    # Here we don't need to be too careful about the robot's gripper being
    # precisely aligned, because it will be tilted as we push it down.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # The gripper is roughly in the right position, so push down to press the
    # button.
    if check("the robot's gripper is above the button"):
        robot.push("down on button")