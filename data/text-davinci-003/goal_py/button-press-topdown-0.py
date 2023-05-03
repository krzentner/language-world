
    # Steps:
    #  1. Move gripper above button
    #  2. Look for the button using the camera
    #  3. Drop gripper above and push down the button
    # First, move the gripper above the button.
    if check("the robot's gripper is not above button"):
        robot.move_gripper("above the button")
    # If the gripper is above the button, look for it with the camera.
    if check("the robot's gripper is above the button and the button is not in view of the camera"):
        robot.look_for("button")
    # If the camera is able to see the button, the gripper should be aligned
    # with it.
    # Push down on the button with the gripper.
    if check("button is in view of the camera and the robot's gripper is vertically aligned with the button"):
        robot.move_gripper("downward", close_gripper=True)