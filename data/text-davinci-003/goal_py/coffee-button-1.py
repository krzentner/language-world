
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because the button on the coffee machine is small, we first need to line
    # up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Once the gripper is lined up, close the gripper to grab onto the button
    # before pushing it.
    if check("the robot's gripper is vertically aligned with button and the robot's gripper is not closed"):
        robot.move_gripper("near the button", close_gripper=True)
    # Now that the gripper has the button trapped, we can push the button.
    if check("the robot's gripper is near button and the robot's gripper is closed"):
        robot.move_gripper("above the button")