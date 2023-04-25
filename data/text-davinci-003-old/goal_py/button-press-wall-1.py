
    # Steps:
    #  1. Line up the gripper with the button from the side
    #  2. Push the button from the front
    # To press the button with a wall in the way, we need to line up the gripper
    # from the side.
    if check("the robot's gripper is not horizontally aligned with the button"):
        robot.move_gripper("horizontally aligned with the button")
    # If the button is aligned with the gripper as seen from in front, we can
    # push the button.
    if check("the robot's gripper is forward aligned with the button"):
        robot.move_gripper("near the button")