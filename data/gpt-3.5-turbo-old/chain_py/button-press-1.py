# Steps:
    #  1. Put gripper in front of the button
    #  2. Grab the button with the gripper
    #  3. Push the gripper forward to press the button
    # First, put the gripper in front of the button.
    if check("the robot's gripper is not in front of the button"):
        robot.place("gripper in front of button")
    # If the gripper isn't around the button, put it around the button.
    if check("the robot's gripper is not around button and the robot's gripper is open"):
        robot.drop("gripper around button")
    # If the gripper is near the button and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near button and the robot's gripper is open"):
        robot.close("gripper around button")
    # We closed the gripper, and the button is still near the gripper, so maybe we
    # grabbed it.
    # Try to push the gripper forward to press the button.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around button"):
        robot.push("forward to press button")