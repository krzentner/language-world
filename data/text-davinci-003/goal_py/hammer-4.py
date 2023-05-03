
    # Steps:
    #  1. Put gripper above hammer
    #  2. Grab hammer with gripper
    #  3. Move gripper to the nail
    #  4. Hit the nail with the hammer
    # Put the gripper above the hammer before picking it up.
    if check("the robot's gripper is not above hammer"):
        robot.move_gripper("above the hammer", close_gripper=True)
    # Once the gripper is above the hammer, line up the gripper with the nail.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Now that the gripper lined up with the nail, hit the nail with the hammer.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.move_gripper("left of the hammer")