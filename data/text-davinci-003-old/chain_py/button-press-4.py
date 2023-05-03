
    # Steps:
    #  1. Put gripper in front of button
    #  2. Push button
    # First, make sure the gripper is in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # If the gripper is aligned with the button as seen from in front, try
    # pushing it.
    # We don't need to be careful from which angle we push, since the robot can
    # come from any angle to press the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button")