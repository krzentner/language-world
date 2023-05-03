
    # Steps:
    #  1. Put gripper forward of button
    #  2. Push button
    # To push a button, we need to line the gripper up in front of the button,
    # because the button needs to be pressed "inward".
    # Put the robot's gripper in front of the button by moving it.
    if check("the robot's gripper is not in front of button"):
        robot.put("gripper forward of button")
    # Now that the gripper is lined up, push the button.
    if check("the robot's gripper is in front of button"):
        robot.push("button")