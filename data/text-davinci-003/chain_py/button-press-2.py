    
    # Steps:
    #  1. Line up gripper with button
    #  2. Push on the button
    # Because this is "button press" we need to line up the gripper from the
    # front.
    if check("the robot's gripper is not forward aligned with the button"):
        robot.put("gripper in front of button")
    # Now that the gripper is lined up, push the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("on button")