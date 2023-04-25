
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Use the wall to push against the button from the top
    #  3. Push down on the button from the top
    # First, line up the robot's gripper from above with the wall in the way.
    if check("the robot's gripper is not almost vertically aligned with button"):
        robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
    # Once the gripper is lined up with the wall in the way, we can use the wall
    # to push against the button.
    if check("the robot's gripper is almost vertically aligned with button and the robot's gripper is not around button"):
        robot.move_gripper("around the button")
    # If the gripper is now around the button, we can push down on the button
    # from the top.
    if check("the robot's gripper is around the button"):
        robot.move_gripper("near the button")