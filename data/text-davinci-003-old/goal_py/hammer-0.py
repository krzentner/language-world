
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Line the hammer up with the nail
    #  4. Swing the hammer to hit the nail
    # First, move the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper isn't around the hammer, put it around the hammer.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("around the hammer", close_gripper=True)
    # If the gripper is around the hammer, we can line it up with the nail.
    if check("the robot's gripper is around the hammer"):
        robot.move_gripper("horizontally aligned with the nail")
    # Once the hammer is lined up, swing it down to hit the nail.
    if check("the robot's gripper is horizontally aligned with the nail"):
        robot.move_gripper("above the nail")