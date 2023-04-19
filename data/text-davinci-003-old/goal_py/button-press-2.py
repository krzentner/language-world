
    # Steps:
    #  1. Put gripper forward of the button
    #  2. Push the button
    # We need to move the gripper forward of the button before pushing it.
    if check("the robot's gripper is not in front of the button"):
        robot.move_gripper("in front of the button")
    # Once the gripper is in front of the button, we can just push on it.
    if check("the robot's gripper is in front of the button"):
        robot.move_gripper("near the button")