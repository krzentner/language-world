
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Line up the hammer and the nail
    #  4. Strike the hammer against the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer", close_gripper=True)
    # If the hammer is not left of the gripper, go back to putting the gripper
    # above the hammer.
    if check("the hammer is not left of the robot's gripper and the hammer is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the hammer")
    # If the hammer is left of the gripper, line it up with the nail.
    if check("the hammer is horizontally aligned with the nail"):
        robot.move_gripper("above the hammer")
    # If the hammer is lined up with the nail, strike the hammer against the
    # nail.
    if check("the robot's gripper is forward aligned with the hammer and the hammer is not horizontally aligned with the nail"):
        robot.move_gripper("horizontally aligned with the nail")