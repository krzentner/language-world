# Steps:
    #  1. Put the gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Line up the hammer with the nail
    #  4. Swing the hammer to hit the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")
    # If the gripper isn't around the hammer, put it around the hammer.
    if check("the robot's gripper is above the hammer and the robot's gripper is not around hammer"):
        robot.move_gripper("around the hammer", close_gripper=True)
    # If the hammer isn't aligned with the nail, align it.
    if check("the hammer is not aligned with the nail"):
        robot.move_gripper("above the nail with the hammer")
    # Swing the hammer to hit the nail.
    if check("the hammer is aligned with the nail"):
        robot.move_gripper("swinging the hammer")