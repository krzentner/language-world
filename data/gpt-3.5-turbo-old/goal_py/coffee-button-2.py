# Steps:
    #  1. Put gripper near the button
    #  2. Push down on the button
    # To push the button, we just need to move the gripper near it and push down.
    if check("the robot's gripper is not near the button"):
        robot.move_gripper("near the button")
    if check("the robot's gripper is near the button"):
        robot.move_gripper("above the button", close_gripper=True)