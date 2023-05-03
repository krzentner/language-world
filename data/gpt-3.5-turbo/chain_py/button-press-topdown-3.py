# Steps:
    #  1. Put gripper above the button
    #  2. Move the gripper down onto the button
    #  3. Push the button to activate it
    # First, put the gripper above the button to avoid hitting anything.
    if check("the robot's gripper is not above the button"):
        robot.move("gripper above button")
    # Move the gripper down onto the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper onto button")
    # Push the button to activate it.
    if check("the robot's gripper is vertically aligned with the button"):
        robot.push("button")