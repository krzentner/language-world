
    # Steps:
    #  1. Line up the gripper as seen from above
    #  2. Push down on the button from the top
    # We just need to line up the gripper so that the button is positioned between
    # the gripper.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # Once the gripper is lined up as seen from above, we can move the gripper
    # kown to push the button.
    if check("the robot's gripper is above the button"):
        robot.move_gripper("near the button")