# Steps:
    #  1. Put gripper above button
    #  2. Move gripper down to press button
    #  3. Lift gripper up off the button
    # First, put the gripper above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If the gripper isn't over the button, we need to move it down to press
    # the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper down to button")
    # If the gripper is aligned with the button, push down to press it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("button down")
    # If the button has been pushed down, we want to lift the gripper up off
    # the button.
    if check("the button is pressed and the robot's gripper is on the button"):
        robot.lift("gripper off button")