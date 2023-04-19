
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Here, because this is "topdown", we just need to line up the gripper from
    # above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # If the gripper is lined up above the button, moving it down a bit will
    # press the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")