# Steps:
    #  1. Put gripper above the coffee machine button
    #  2. Drop gripper around the button
    #  3. Push the button
    # First, put the gripper above the coffee machine button.
    if check("the robot's gripper is not above the coffee machine button"):
        robot.move_gripper("above the coffee machine button")
    # If the gripper is above the button, drop it around the button.
    if check("the robot's gripper is above the coffee machine button and the robot's gripper is not around the button"):
        robot.move_gripper("around the coffee machine button", close_gripper=True)
    # Once the gripper is around the button, push the button.
    if check("the robot's gripper is around the coffee machine button"):
        robot.move_gripper("near the coffee machine button")