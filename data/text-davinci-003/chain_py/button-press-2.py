
    # Steps:
    #  1. Put the gripper near the button
    #  2. Push the button
    # First, move the robot's gripper near the button, either from higher up or
    # from the sides.
    if check("the robot's gripper is not near button"):
        robot.move("gripper to button")
    # If the robot's gripper is near the button and alligned with the button,
    # we can press the button by pushing forward.
    if check("the robot's gripper is near button and the robot's gripper is forward aligned with button"):
        robot.push("button")