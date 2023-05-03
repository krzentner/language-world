
    # Steps: 
    #  1. Put gripper above the hammer
    #  2. Lift the hammer up
    #  3. Line up the hammer with the nail
    #  4. Hit the nail with the hammer
    # First, move the robot's gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper isn't around the hammer, put it around the hammer.
    # We don't have to worry about any other direction, since the hammer is a
    # small object.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # As long as the hammer is mostly in front of the nail, line up the hammer
    # with the nail.
    if check("the hammer is forward aligned with the nail"):
        robot.move_gripper("above the hammer")
    # If the hammer is lined up with the nail, hit the nail with the hammer.
    if check("the robot's gripper is forward aligned with the hammer and the hammer is not forward aligned with the nail"):
        robot.move_gripper("nail with hammer")