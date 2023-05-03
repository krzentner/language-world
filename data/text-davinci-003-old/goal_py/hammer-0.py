
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop gripper around the hammer
    #  3. Align the hammer with the nail
    #  4. Hit the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper is not around the hammer, line it up and grab it.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("around the hammer", close_gripper=True)
    # Now that we have the hammer and it's in the gripper, we can line it up
    # with the nail.
    # This requires a little bit of trial and error since the gripper movement
    # is limited.
    if check("the hammer is not vertically aligned with nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Once the hammer is lined up with the nail, we can hit the nail.
    if check("the hammer is vertically aligned with nail"):
        robot.move_gripper("above the hammer")