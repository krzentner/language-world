
    # Steps:
    #  1. Put gripper above the button
    #  2. Push the button down
    # First, try to put the gripper around the button so we can push it down with
    # the tool tip.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # Once the gripper is lined up above the button, we can push it down by
    # opening the gripper slightly and pressing down on the button with the tool
    # tip.
    if check("the robot's gripper is above the button"):
        robot.push("gripper into button")