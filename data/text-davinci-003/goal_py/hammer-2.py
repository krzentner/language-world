
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Drop gripper around the hammer
    #  3. Move the gripper to hold the hammer
    #  4. Move gripper-held-hammer towards nail
    #  5. Hit the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.move_gripper("above the hammer")
    # If the gripper isn't around the hammer, move it around the hammer until it
    # is.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.move_gripper("around the hammer", close_gripper=True)
    # If the hammer is close to the nail, hit the nail by quickly moving the
    # gripper-held-hammer towards the nail.
    if check("the robot's gripper is holding the hammer and the hammer is near the nail"):
        robot.move_gripper("forward aligned with the nail", close_gripper=True, fast_grip_speed=True)