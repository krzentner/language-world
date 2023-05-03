# Steps:
    #  1. Put gripper above button
    #  2. Drop gripper onto button
    #  3. Push button down
    # First, put the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the gripper is above the button, drop it onto the button.
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not touching the button"):
        robot.move_gripper("on top of the button")
    # If the gripper is on top of the button, push the button down.
    if check("the robot's gripper is touching the button"):
        robot.move_gripper("above the button")