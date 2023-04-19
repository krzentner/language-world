# Steps:
    #  1. Put gripper in front of button
    #  2. Push down on the button
    # The robot needs to be aligned with the button from the front to push it.
    # Move the gripper to be in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.move("gripper to front of button")
    # Once the gripper is in front of the button, just push down on the button.
    if check("the robot's gripper is in front of the button"):
        robot.push("down on button")