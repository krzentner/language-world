
    # Steps:
    #  1. Put gripper in front of button
    #  2. Push down on the button
    # We should start by putting the robot's gripper in front of the button.
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")
    # Once the gripper is in front of the button, start pushing down on it.
    if check("the robot's gripper is forward aligned with button"):
        robot.push("down on button")