
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the button
    # First, move the gripper above the button. This makes it easier to control
    # the pushing motion.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # When the gripper is in place, just push the button.
    if check("the robot's gripper is above button"):
        robot.push("button")