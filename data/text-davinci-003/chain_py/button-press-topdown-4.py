
    # Steps:
    #  1. Put gripper above button
    #  2. Push gripper down onto button
    #  3. Push the button down
    # First, move the gripper so that it is above the button.
    if check("the robot's gripper is not above button and the robot's gripper is not vertically aligned with button"):
        robot.move("gripper above button")
    # If the gripper is above the button but not near it, move the gripper
    # downwards onto the button.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not near button"):
        robot.push("gripper onto the button")
    # Once the gripper is on the button, we need to push the button downwards.
    if check("the robot's gripper is near button"):
        robot.push("button downwards")