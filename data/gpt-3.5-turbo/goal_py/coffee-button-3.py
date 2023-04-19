# Steps:
    #  1. Put gripper above the button
    #  2. Push down on the button
    # The robot just needs to position the gripper above the coffee machine's button and then push down on it.
    # Move the gripper above the button.
    if check("the robot's gripper is not vertically aligned with the coffee machine button"):
        robot.move_gripper("vertically aligned with the coffee machine button")
    # Push down on the button.
    if check("the robot's gripper is vertically aligned with the coffee machine button"):
        robot.move_gripper("near the coffee machine button")