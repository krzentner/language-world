
    # Steps:
    #  1. Put gripper above the button
    #  2. Push gripper down onto button
    #  3. Push button down
    # We will start off by roughly aiming the gripper above the button, so as
    # not to bump it while trying to press it.
    if check("the robot's gripper is not above the button"):
        robot.move_gripper("above the button")
    # If the gripper has the button below it, we can push down on it to push the
    # button.
    if check("the robot's gripper is now above the button and the button is below the robot's gripper"):
        robot.move_gripper("below the button")
    # Once the button has been pushed down, we should move the gripper away from
    # the button to make sure it stays down.
    if check("the robot's gripper is below the button"):
        robot.move_gripper("above the button")