# Steps:
    #  1. Line up the gripper as viewed from above, near the wall
    #  2. Move the gripper forward, above the button
    #  3. Push down on the button from the top
    # Because there's a short wall in the way, we need to position the gripper
    # closer to the wall before we can line it up with the button from above.
    # Line up the robot's gripper from above, near the wall.
    if check("the robot's gripper is not vertically aligned with button and is right of the wall"):
        robot.move_gripper("almost vertically aligned with the button, right of the wall", close_gripper=True)
    # Once the gripper is near the wall and almost lined up with the button,
    # move it forward above the button.
    if check("the robot's gripper is vertically aligned with the button and is right of the wall"):
        robot.move_gripper("almost above the button", close_gripper=True)
    # Now that the gripper is above the button, just push down on the button.
    if check("the robot's gripper is near the button and is right of the wall"):
        robot.move_gripper("on top of the button")