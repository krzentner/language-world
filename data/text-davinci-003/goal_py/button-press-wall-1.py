
    # Steps:
    #  1. Put gripper at end of wall
    #  2. Line up gripper with the button
    #  3. Push the button
    # First, put the gripper at the end of the wall.
    if check("the robot's gripper is not at the end of the wall"):
        robot.move_gripper("at the end of the wall")
    # If the gripper isn't lined up with the button, move the gripper up until
    # it is.
    # The wall may have gotten in the way, so we don't mind if the gripper is
    # above the wall a bit.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button")
    # Now that the gripper is lined up with the button, just push the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("forward aligned with the button")