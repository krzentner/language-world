
    # Steps:
    #  1. Put gripper above the button
    #  2. Press down on the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Once the gripper is over the button, just press down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.press("down on button")