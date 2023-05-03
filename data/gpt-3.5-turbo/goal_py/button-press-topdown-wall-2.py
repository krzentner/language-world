# Steps:
    #  1. Line up the gripper as viewed from above with the button
    #  2. Move the gripper forward, over the wall, until the gripper is above the button
    #  3. Push down on the button from the top
    # First, line up the robot's gripper from above with the button.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Next, move the gripper forward, over the wall, until the gripper is above
    # the button.
    if check("the robot's gripper is not above the wall and the robot's gripper is vertically aligned with button"):
        robot.move_gripper("above the wall", close_gripper=True)
    # Once the gripper is over the wall and above the button, push down on the button.
    if check("the robot's gripper is forward aligned with button"):
        robot.move_gripper("near the button")