# Steps:
    #  1. Put gripper above button
    #  2. Push down on button
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee button"):
        robot.put("gripper above coffee button")
    # Once the gripper is above the button, push down on the button.
    if check("the robot's gripper is vertically aligned with the coffee button"):
        robot.push("down on coffee button")