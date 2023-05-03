
    # Steps:
    #  1. Put gripper above button
    #  2. Push the button down
    # First, put the gripper just slightly above the button.
    if check("the robot's gripper is not almost vertically above button"):
        robot.put("gripper almost above button")
    # If it's lined up, push the button down.
    if check("the robot's gripper is almost vertically above button"):
        robot.push("down the button")