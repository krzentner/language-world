# Steps:
    #  1. Put gripper in front of button
    #  2. Push down on the button
    # Since we're pushing from the front, we just need to put the gripper in
    # front of the button.
    if check("the robot's gripper is not in front of button"):
        robot.move_gripper("in front of the button", close_gripper=True)
    # Once the gripper is in front of the button, we can just push down on it.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")